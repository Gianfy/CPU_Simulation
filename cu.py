# This is a simulation of the CU component of a MIPS32 architecture cpu

# Binary instruction format
# TypeR  000000 00000 00000 00000 00000 000000   op = 000000 refers to func
#          OP     rs    rt   rd   shamt  func
# TypeI  000000 00000 00000 0000000000000000
#          OP    rs    rt       immd
# TypeJ  000000 00000 00000 0000000000000000
#          OP    rs    rt       offset(it's in byte) 


# Remember all addres in binary code are the registers address in the CPU
from ram import RAM

from registers import REGISTERS
from alu import ALU

class CU:
    def __init__(self, registers_object, alu_object, binary_code):
        self.binary_code = binary_code
        self.opcode = ''
        self.source_one = ''
        self.source_two = ''
        self.destination = ''
        self.alu = alu_object
        self.registers = registers_object
        self.ram = RAM(32)

    def decode_binary_code(self):
        self.opcode = self.binary_code[:6]

        if self.opcode == '000000':
            # This is TypeR instruction case
            # the real opcode is 'func'
            self.source_one = self.binary_code[6:11]
            self.source_two = self.binary_code[11:16]
            self.destination = self.binary_code[16:21]
            self.opcode = self.binary_code[26:]
        else:
            # This is TypeI instruction case
            # source_one = rs source_two = immd destination = rt
            self.source_one = self.binary_code[6:11]
            self.destination = self.binary_code[11:16]
            # This is an immediate value
            self.source_two = self.binary_code[16:]

        # Decoding produces the set of elements necessary for the required operations
        return (self.opcode, self.source_one, self.source_two, self.destination)


    # This method is combined with loading from memory, i.e. the LOAD operation
    def store_value_in_register(self, destination, value_to_store):
        index = int(destination, 2)
        self.registers.mem[index] = bin(int(value_to_store, 2))
        
        action = f'store value {int(value_to_store, 2)} in register {int(destination, 2)}'
        self.registers.update_status(action)

    
    # get values to alu operations
    def get_value_from_register(self, source):
        value = self.registers.mem[int(source, 2)]
        action = f'get value {int(value, 2)} from register {int(source, 2)}'
        self.registers.update_status(action)
        return value


    def alu_activation(self):
        value_one = self.get_value_from_register(self.source_one)
        value_two = self.get_value_from_register(self.source_two)

        # Activate the alu to perform the calculations
        result = self.alu.get_opcode_and_values_from_cu(self.opcode, value_one, value_two)
        return result

    
    def execute_binary_code(self):
        # valutare l'opcode per capire come gestire i risultati della alu
        result = self.alu_activation()
        
        if self.opcode == '000100':
            # load from memory to store in registry operation
            value_from_memory = self.get_value_from_memory(result)
            self.store_value_in_register(self.destination, value_from_memory)
        elif self.opcode == '000110':
            # store from register to memory operation
            self.get_value_from_register(self.destination)
            self.store_value_to_memory(result)
        else:
            self.store_value_in_register(self.destination, result)
    

    def store_value_to_memory(self, address):
        ...

        
    def get_value_from_memory(self, addres):
        index = int(addres, 2)
        value_get = self.ram.mem[index]
        action = f'get value {int(value_get, 2)} from memory {int(addres, 2)}'
        self.ram.update_status(action)
        return value_get

def main():
    # Testing object
    binary_code = '00000000010000010001100000000001'
    reg = REGISTERS(32)
    alu = ALU()
    test = CU(reg, alu, binary_code)
    print(test.get_value_from_memory('00111'))


