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


class ALU:
    def __init__(self, opcode, source_one, source_two):
        self.opcode = opcode
        self.source_one = source_one
        self.source_two = source_two


    def add_op(self, opcode, source_one, source_two): 
        return self.source_two + self.source_one

    def sub_op(self, opcode, source_one, source_two):
        return self.source_two - self.source_one
    
    def mult_op(self, opcode, source_one, source_two):
        return self.source_two * self.source_one

    def execute_op(self):
        if opcode == '000001':
            self.add_op()
        elif opcode == '000010':
            self.sub_op()
        elif opcode == '000011':
            self.mult_op()
        