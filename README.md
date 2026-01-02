# CPU_Simulation

Very simple simulation of the behavior of a CPU (of the MIPS32 type).
The deliberately simplified project serves to show the processor instruction cycle (fetch, decode, execute), the interaction between the various internal components and memories (cu, alu, registers, cache, ram) and some examples of instructions in binary code.

## Current status
-Implementation: add, sub, mul, load (from Ram to register), store (from register to Ram) via cache.
-Jumps and other flow control instructions are missing; better management of formats and types.
-As regards the Cache, Directed-Mapped for associativity and Write-back for the write policy have been expanded. It is possible to implement the other policies in the future.

## Requirements
-Python 3.8+ (no external dependencies).

## Quick use
1. Go to the root of the repository (where 'simulation.py' is)
2. Run:

    ```markdown
        python3 simulation.py input.txt
    ```

Where 'input.txt' is the file with instructions in binary format.

## Input file format
-Each line contains an instruction in binary code (32-bit string) according to a MIPS32 format:

    
    -typeR -- op(6 bit) rs(5 bit) rt(5 bit) rd(5 bit) shamt(5 bit) FUNC(6 bit)

    -typeI -- op(6 bit) rs(5 bit) rt(5 bit) imd(16 bit) [rt destination]    

    -typeJ -- op(6 bit) rs(5 bit) rt(5 bit) offset(16 bit) [rt destination or source in SW]
    
    
-The input file shows an example of a test format. It wants to simulate a possible file in assembly format which was hypothetically transformed into binary line by line and which for the moment is directly executed instruction by instruction. (the possibility of loading it into RAM from which it would then be read similarly to reality will be implemented).

## Outputs
-The program prints in the console the logs of the operations it is carrying out on the memories, registers, cache phases and access to the lau. (all data is in full format to be a little more readable)

Example output:
    
    
    Decoding the instruction 00010000000000010000000000001010: 
    Opcode: 000100, soure_one: 00000, source_two: 0000000000001010, destination: 00001

    Access to Registers: get value 0 from register at address 0
    Activation ALU: add value 10 with value 0. Result is the memory address 10
    Access to Main Memory: get value 25 from memory at address 10
    Cache MISS!  Access to Cache: store value 25 to cache at address 10
    Access to Registers: store value 25 in register at address 1
    

## Implementation choices
-It was chosen to try to get a little closer to the reality of using the string type to represent data in binary format ('0b00' or '00').

-The manipulation in the operations occurs with the transformation into integers to indicate the numerical values ​​and therefore the memory indices in the data structures.

-For load and store operations the data must always be represented as binary in the form of strings.

-The data structure used for memories is the list while for the cache it is a list of dictionaries ([{'Tag': , 'Data': , 'Dirty_Bit'}])


## Future implementation attempts
-Add new instructions.
-Implement instruction file loading into main memory. (closer to reality).


## How to contribute
-I would be happy if there were corrections and improvements by those who are more expert even proposing a distortion of the general logic if (as is presumable) it is found that my logic is too crude and not very functional.
-Thank you for your help and willingness to educate me to do better.


## License
-Study and learning project