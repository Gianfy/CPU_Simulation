# This is the simulation of a CPU in overall terms.
# It will consist of an ALU and a CU.

class CPU:
    def __init__(self, binary_code):
        self.binary_code = binary_code
        self.registers = [{address: ''} for addres in range(32)]
        