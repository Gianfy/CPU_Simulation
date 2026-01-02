# The project is a very basic simulation of operation with many approximations
# of the functioning of a CPU and its components including the main memory.
# The software is designed as the present file which represents the Front-end and all the classes
# which represent the computer, the cpu, the cu, the alu and the memories starting from the registers to the cache up to the ram.
# This software will read input from a text file which must contain all instructions in binary code
# based on the MIPS architecture.
# For the moment the instructions inserted are only addition, subtraction, multiplication, loading from main memory into registers and
# saving registers to main memory, all via cache memory.
# There are no Assembly instructions planned for the moment, they could be included for a future implementation.
# The software shows as output on the console everything that happens in the memories, showing the values not in binary format but with integers
# The input file is expected directly from the command line as a call argument.
# Have fun!!

from Simple_computer_simulation import COMPUTER_SIMULATION
from sys import argv


def main():
    if len(argv) < 2:
        print("No arguments. Type of use: 'python3 simulation.py <instructions_file.txt>'")
        return 1
    file_in = argv[1]

    computer = COMPUTER_SIMULATION("Gianni", 32)
   
    computer.input_from_user(file_in)
    computer.power_on()


if __name__ == "__main__":
    main()