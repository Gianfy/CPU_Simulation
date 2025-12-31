# Questa classe simula il comportamento generale di qualunque memoria
# L'argomento arch indica l'architettura della memoria quindi lo idicherò come un int
class MEMORY:
    def __init__(self, arch):
        self.arch = arch
        self.mem = [str(bin(_)) for _ in range(self.arch)]
        

    def action_on_memory(self, type_memory):
        print(f'Access to {type_memory}: ', end=' ')



