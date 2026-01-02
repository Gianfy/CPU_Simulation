# Questa rappresenta una semplicissima simulazione di un computer per motivi di studio.
# Per il momento le componenti si mantengono nella semplicità di operazioni come somma, sottrazione e moltiplicazione.
# Saraà necessario inserire l'operazione di Salto per poter testare anche l'uso del PC(program counter).
# Questa classe rappresenta il Computer nella sua totalità, i componenti sono in classi separate e sono:
# CPU, CU, Memorie(registri, cache e ram), ALU.
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