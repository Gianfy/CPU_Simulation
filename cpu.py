# This is the simulation of a CPU in overall terms.
# It will consist of an ALU and a CU.
# The instruction cycle of the cpu is simplified to three phases, I foreseen memory access in the execute phase

from cu import CU
from alu import ALU
from registers import REGISTERS
from cache import CACHE

class CPU:
    def __init__(self, binary_code, arch):
        self.binary_code = binary_code
        self.alu = ALU()
        self.registers = REGISTERS(arch)
        self.cache = CACHE(arch)
        self.cu = ''
        self.cycle_stage = 0

    def cpu_instruction_cycle(self):
        
        while self.cycle_stage <= 2:
            
            if self.cycle_stage == 0:
                # Fetch
                self.cu = CU(self.registers, self.alu, self.cache, self.binary_code)
            elif self.cycle_stage == 1:
                # Decode
                self.cu.decode_binary_code()
            elif self.cycle_stage == 2:
                # Execute
                self.cu.execute_binary_code()
            
            self.cycle_stage += 1








def main():
    binary_code = '000110000000001100000000000000010'
    test_cpu = CPU(binary_code, 32)
    test_cpu.cpu_instruction_cycle()

if __name__ == "__main__":
    main()