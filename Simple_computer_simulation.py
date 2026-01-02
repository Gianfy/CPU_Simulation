# Questa rappresenta una semplicissima simulazione di un computer per motivi di studio.
# Per il momento le componenti si mantengono nella semplicità di operazioni come somma, sottrazione e moltiplicazione.
# Saraà necessario inserire l'operazione di Salto per poter testare anche l'uso del PC(program counter).
# Questa classe rappresenta il Computer nella sua totalità, i componenti sono in classi separate e sono:
# CPU, CU, Memorie(registri, cache e ram), ALU.
from cpu import CPU


class COMPUTER_SIMULATION:
    def __inti__(self, name, arch):
        self.name = name
        self.cpu = CPU(arch)
        self.instructions = []

    
    def input_from_user(self, file):
        with open(file) as file:
            self.instructions = file.readlines()

    def power_on(self):
        self.cpu.cpu_instruction_cycle(self.instructions)        



def main():
    computer = COMPUTER_SIMULATION('Gianni', 32)
    istructions = computer.input_from_user('test.txt')
    computer.power_on()