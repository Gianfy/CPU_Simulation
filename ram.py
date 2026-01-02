# This class represents a simulation of RAM (Random Access Memory) in a PC
# for simplicity I will set the size to 32 memory addresses

from memory import MEMORY

class RAM(MEMORY):

    def __init__(self, arch):
        super().__init__(arch * 2)
        self.name = "Main Memory"

    """
    def update_status(self, action):
        self.action_on_memory(self.name)
        print(action)
    """

    
def main():
    test = RAM(32)
    test.show_status_mem()

if __name__ == "__main__":
    main()





