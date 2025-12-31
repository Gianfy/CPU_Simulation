# Questa classe rappresenta una simulazione della RAM (Random Access Memory) in un PC
# per semplicità imposterò la gandezza a 32 indirizzi di memoria


from memory import MEMORY

class RAM(MEMORY):
    
    def __init__(self, arch):
        super().__init__(arch)
        self.name = "Ram"

    def update_status(self, action):
        self.action_on_memory(self.name)
        print(action)


    






