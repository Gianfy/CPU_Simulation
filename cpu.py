# This is the simulation of a CPU in overall terms.
# It will consist of an ALU and a CU.
from cu import CU
from alu import ALU
from registers import REGISTERS

class CPU:
    def __init__(self, binary_code, arch):
        self.binary_code = binary_code
        self.alu = ALU()
        self.registers = REGISTERS(arch)
        self.cu = CU(self.registers, self.alu, self.binary_code)


    





def main():
    binary_code = '000110000000001100000000000000010'
    test_cpu = CPU(binary_code, 32)
    result = test_cpu.cu.decode_binary_code()
    print(result)
    test_cpu.cu.execute_binary_code()

if __name__ == "__main__":
    main()