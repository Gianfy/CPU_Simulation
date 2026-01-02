# This is a simulation of a simple cache memory consisting of 8 blocks for initial simplicity
from memory import MEMORY

class CACHE(MEMORY):

    def __init__(self, arch):
        super().__init__(arch)
        # I have foreseen in addition to the tag that contains the ram address and the corresponding data also the Dirty modification bit
        self.mem = [{'Tag': '', 'Data': '', 'Dirty_Bit': '0'} for _ in range(arch)]
        self.name = "Cache"
        self.blocks_numbers = arch

    """
    def update_status(self, action):
        self.action_on_memory(self.name)
        print(action)
    """

    def get_blocks_numbers(self):
        return self.blocks_numbers
    

def main():
    test = CACHE(32)
    print(test.show_status_mem())


if __name__ == "__main__":
    main()