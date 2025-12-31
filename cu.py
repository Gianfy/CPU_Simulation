# This is a simulation of the CU component of a MIPS32 architecture cpu

# Binary instruction format
# TypeR  000000 00000 00000 00000 00000 000000   op = 000000 refers to func
#          OP     rs    rt   rd   shamt  func
# TypeI  000000 00000 00000 0000000000000000
#          OP    rs    rt       immd
# TypeJ  000000 00000000000000000000000000
#          OP          address 


class CU:
    def __init__(self, binary_code):
        self.binary_code = binary_code
        self.opcode = ''
        self.source_one = ''
        self.source_two = ''
        self.destination = ''


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
            self.source_two = self.binary_code[16:]

    def send_opcode_to_alu(self):
        return self.opcode

    def get_values_from_memory(self):
        return ()

    def store_values_to_memory(self):
        ...


# Testing object
binary_code = '00000000010000010001100000000001'
first_cu = CU(binary_code)
first_cu.decode_binary_code()
opcode = first_cu.send_opcode_to_alu()

print(opcode)
print(first_cu.source_one)
print(first_cu.source_two)
print(first_cu.destination)