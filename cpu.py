# This is the simulation of a CPU in overall terms.
# It will consist of an ALU and a CU.
# The instruction cycle of the cpu is simplified to three phases, I foreseen memory access in the execute phase

from cu import CU
from alu import ALU
from registers import REGISTERS
from cache import CACHE
from ram import RAM

class CPU:
    def __init__(self, arch):
        self.alu = ALU()
        self.registers = REGISTERS(arch)
        self.cache = CACHE(arch)
        self.ram = RAM(arch)
        self.cu = CU(self.registers, self.alu, self.cache, self.ram)
        self.cycle_stage = 0

    def cpu_instruction_cycle(self, binary_code):
        
        while self.cycle_stage <= 2:
            
            if self.cycle_stage == 0:
                # Fetch
                self.cu.fetch_operation(binary_code)
            elif self.cycle_stage == 1:
                # Decode
                self.cu.decode_binary_code()
            elif self.cycle_stage == 2:
                # Execute
                self.cu.execute_binary_code()
            
            self.cycle_stage += 1








def main():
    binary_code = '000110000000001100000000000000010'
    
    test_cpu = CPU(32)
    
    test_cpu.ram.show_status_mem()    
    test_cpu.cache.show_status_mem()
    
    test_cpu.cpu_instruction_cycle(binary_code)

    test_cpu.ram.show_status_mem()    
    test_cpu.cache.show_status_mem()
    

if __name__ == "__main__":
    main()