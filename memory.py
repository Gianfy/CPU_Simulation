# This class simulates the general behavior of any memory
# The arch argument indicates the memory architecture so I will refer to it as an int
from random import randint
class MEMORY:
    def __init__(self, arch):
        self.arch = arch
        # tutte le memorie di base sono riempite in modo casuale
        self.mem = [bin(randint(0, 31)) for _ in range(self.arch)]
        self.name = ''

    def update_status(self, action):        
        print(f'Access to {self.name}: {action}')

    def action_on_memory(self, type_memory):
        print(f'Access to {type_memory}: ', end=' ')
    
    def show_status_mem(self):
        print(self.mem)


