# This is the simulation of an ALU inside a CPU with MIPS architecture
# Being a study project for the moment it only contains some basic instructions
# for arithmetic operations, data loading and storage.
# Instructions:

# instruction    Operand            Meaning
# ADD            Rd, Rs, Rt         Rd <-- Rs + Rt
# ADDI           Rt, Rs, Immd       Rt <-- Rs + Immd
# SUB            Rd, Rs, Rt         Rd <-- Rs - Rt
# LW             Rt, offset(Rs)     Rt <-- MEM[Rs + offset]
# SW             Rt, offset(Rs)     MEM[Rs + offset] <-- Rt   

# Binary instruction format
# TypeR  000000 00000 00000 00000 00000 000000   op = 000000 refers to func
#          OP     rs    rt   rd   shamt  func
# TypeI  000000 00000 00000 0000000000000000
#          OP    rs    rt       immd
# TypeJ  000000 00000000000000000000000000
#          OP          address 

class ALU:
    def __init__(self, opcode, source_one, source_two):
        self.opcode = opcode
        self.source_one = source_one
        self.source_two = source_two


    def add_op(self): 
        return self.source_two + self.source_one

    def sub_op(self):
        return self.source_two - self.source_one
    
    def mult_op(self):
        return self.source_two * self.source_one

    def execute_op(self):
        if opcode == '000001':
            self.add_op()
        elif opcode == '000010':
            self.sub_op()
        elif opcode == '000011':
            self.mult_op()
        