# This class simulates the internal memory registers of the CPU
from memory import MEMORY

class REGISTERS(MEMORY):

    def __init__(self, arch):
        super().__init__(arch)
        self.mem = [bin(_) for _ in range(arch)]
        self.name = "Registers"

    """
    def update_status(self, action):
        self.action_on_memory(self.name)
        print(action)
    """
