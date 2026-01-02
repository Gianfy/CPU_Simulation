# This is the simulation of an ALU (Arithmetic Logic Unit) inside a CPU with MIPS architecture
# Being a study project for the moment it only contains some basic instructions
# for arithmetic operations, data loading and storage.
# Instructions:

# instruction    Operand            Meaning
# ADD            Rd, Rs, Rt         Rd <-- Rs + Rt
# ADDI           Rt, Rs, Immd       Rt <-- Rs + Immd
# SUB            Rd, Rs, Rt         Rd <-- Rs - Rt
# LW             Rt, offset(Rs)     Rt <-- MEM[Rs + offset]
# SW             Rt, offset(Rs)     MEM[Rs + offset] <-- Rt   


# remember source_one and source_two must be values in registers of CPU

class ALU:
    
    
    def __init__(self):
        self.opcode = ''
        self.source_value_one = ''
        self.source_value_two = ''
        self.status = "Activation ALU for operation: "


    def get_opcode_and_values_from_cu(self, opcode, source_value_one, source_value_two):
        # Collects the values ​​contained in the registers passed to it by the CU in string format and the opcode
        self.opcode = opcode
        self.source_one = source_value_one
        self.source_two = source_value_two

        result_value = self.execute_op()
        return result_value

    def add_op(self):
        # Calculates the operation and returns a value in binary not as a string
        # receives the values contained in the registers as arguments
        result_value = bin(int(self.source_two, 2) + int(self.source_one, 2))
        action = f'add value {int(self.source_two, 2)} with value {int(self.source_one, 2)}'
        print(self.status + action)
        return result_value

    def sub_op(self):
        # Calculates the operation and returns a value in binary not as a string
        # receives the values contained in the registers as arguments
        result_value = bin(int(self.source_two, 2) - int(self.source_one, 2))
        action = f'sub value {int(self.source_two, 2)} with value {int(self.source_one, 2)}'
        print(self.status + action)
        return result_value

    def mult_op(self):
        # Calculate the operation and return a value in binary not as a string
        # receives the values contained in the registers as arguments
        result_value = bin(int(self.source_two, 2) * int(self.source_one, 2))
        action = f'mult value {int(self.source_two, 2)} with value {int(self.source_one, 2)}'
        print(self.status + action)
        return result_value

    def load_op(self):
        # Receives the offset + contents of register 1 as arguments
        memory_address = bin(int(self.source_two, 2) + int(self.source_one, 2))
        action = f'add value {int(self.source_two, 2)} with value {int(self.source_one, 2)}. Result is the memory address {int(memory_address, 2)}'
        print(self.status + action)
        return memory_address

    def store_op(self):
        # Receives the offset + contents of register 1 as arguments
        memory_address = bin(int(self.source_two, 2) + int(self.source_one, 2))
        action = f'add value {int(self.source_two, 2)} with value {int(self.source_one, 2)}. Result is the memory address {int(memory_address, 2)}'
        print(self.status + action)
        return memory_address


    def execute_op(self):
        result = ''
        # Evaluate the opcode and perform operations
        if self.opcode == '000001':
            result = self.add_op()
        elif self.opcode == '000010':
            result = self.sub_op()
        elif self.opcode == '000011':
            result = self.mult_op()
        elif self.opcode == '000100':
            result = self.load_op()
        elif self.opcode == '000110':
           result =  self.store_op()
        return result


        print(status + action)