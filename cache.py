#This is a simulation of a simple cache memory consisting of 8 blocks for initial simplicity
from memory import MEMORY

class CACHE(MEMORY):

    def __init__(self, arch):
        super().__init__(arch)
        self.mem = [{'Tag': '', 'Data': ''} for _ in range(arch)]
        self.name = "Cache"

    def update_status(self, action):
        self.action_on_memory(self.name)
        print(action)


    