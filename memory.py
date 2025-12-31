# Questa classe simula il comportamento generale di qualunque memoria
# L'argomento arch indica l'architettura della memoria quindi lo idicherò come un int
class MEMORY:
    def __init__(self, arch):
        self.arch = arch
        self.mem = [0 for _ in range(self.arch)]
        self.update = 'Access to memory: '
