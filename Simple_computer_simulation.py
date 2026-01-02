# This represents a very simple simulation of a computer for study purposes.
# For the moment the components maintain the simplicity of operations such as addition, subtraction and multiplication.
# It will be necessary to insert the Jump operation in order to also test the use of the PC (program counter).
# This class represents the Computer as a whole, the components are in separate classes and are:
# CPU, CU, Memories (registers, cache and ram), ALU.
# Il computer simulato
from cpu import CPU

class COMPUTER_SIMULATION:
    def __init__(self, name, arch):
        self.name = name
        self.cpu = CPU(arch)
        self.instructions = []

    
    def input_from_user(self, file):
        with open(file) as file:
            for line in file:
                self.instructions.append(line.strip())

    def power_on(self):
        for code in self.instructions:
            self.cpu.cpu_instruction_cycle(code)        



def main():
    computer = COMPUTER_SIMULATION('Gianni', 32)
    istructions = computer.input_from_user('test.txt')
    print(computer.instructions)
    computer.power_on()

if __name__ == "__main__":
    main()