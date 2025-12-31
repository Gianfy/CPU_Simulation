# Questa classe simulai registri interni di memoria della CPU 
from memory import MEMORY

class REGISTERS(MEMORY):

    def __init__(self, arch):
        super().__init__(arch)
        self.name = "Registers"

    def update_status(self, action):
        self.action_on_memory(self.name)
        print(action)

