# Questa classe simula il comportamento generale di qualunque memoria
# L'argomento arch indica l'architettura della memoria quindi lo idicherò come un int
class MEMORY:
    def __init__(self, arch):
        self.arch = arch
        self.mem = [bin(0) for _ in range(self.arch)]
        self.name = ''

    def update_status(self, action):        
        print(f'Access to {self.name}: {action}')

    def action_on_memory(self, type_memory):
        print(f'Access to {type_memory}: ', end=' ')
    
    def show_status_mem(self):
        print(self.mem)


