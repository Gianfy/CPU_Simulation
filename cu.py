# This is a simulation of the CU (Control Unit) component of a MIPS32 architecture cpu

# Binary instruction format
# TypeR  000000 00000 00000 00000 00000 000000   op = 000000 refers to func
#          OP     rs    rt   rd   shamt  func
# TypeI  000000 00000 00000 0000000000000000
#          OP    rs    rt       immd
# TypeJ  000000 00000 00000 0000000000000000
#          OP    rs    rt       offset(it's in byte) 

# I have foreseen in the implementation that the data are all binary strings, they are transformed into integers only 
# in log events
# Remember all address in binary code are the registers address in the CPU
from ram import RAM

class CU:
    def __init__(self, registers_object, alu_object, cache_object, ram_object):
        self.binary_code = ''
        self.opcode = ''
        self.source_one = ''
        self.source_two = ''
        self.destination = ''
        self.alu = alu_object
        self.registers = registers_object
        self.cache = cache_object
        self.ram = ram_object
        # I inserted a bit that differentiates the R operation type from the others
        self.immd_bit = 0
    
    def show_status_ram(self):
        self.ram.show_status_mem()

    def show_status_cache(self):
        self.cache.show_status_mem()

    def fetch_operation(self, binary_code):
        self.binary_code = binary_code

    def decode_binary_code(self):
        self.opcode = self.binary_code[:6]

        if self.opcode == '000000':
            # This is TypeR instruction case
            # the real opcode is 'func'
            self.source_one = self.binary_code[6:11]
            self.source_two = self.binary_code[11:16]
            self.destination = self.binary_code[16:21]
            self.opcode = self.binary_code[26:]
        else:
            # This is TypeI or Type J instruction case
            # source_one = rs source_two = immd destination = rt
            self.source_one = self.binary_code[6:11]
            self.destination = self.binary_code[11:16]
            # This is an immediate value or offset
            self.source_two = self.binary_code[16:]
            # Set immediate bit to 1
            self.immd_bit = 1

        # Decoding produces the set of elements necessary for the required operations
        return (self.opcode, self.source_one, self.source_two, self.destination)


    # This method is combined with loading from memory, i.e. the LOAD operation
    def store_value_in_register(self, destination, value_to_store):
        index = int(destination, 2)
        self.registers.mem[index] = bin(int(value_to_store, 2))
        
        action = f'store value {int(value_to_store, 2)} in register at address {int(destination, 2)}'
        self.registers.update_status(action)

    
    # get values to alu operations
    def get_value_from_register(self, source):
        value = self.registers.mem[int(source, 2)]
        action = f'get value {int(value, 2)} from register at address {int(source, 2)}'
        self.registers.update_status(action)
        return value


    def alu_activation(self):
        value_one = self.get_value_from_register(self.source_one)
        if self.immd_bit == 1:
            value_two = self.source_two
            # Set immd bit to 0 for next istruction
            self.immd_bit = 0
        else:
            value_two = self.get_value_from_register(self.source_two)
            self.immd_bit = 0

        # Activate the alu to perform the calculations
        result = self.alu.get_opcode_and_values_from_cu(self.opcode, value_one, value_two)
        return result

    
    def execute_binary_code(self):
        # valutare l'opcode per capire come gestire i risultati della alu
        result = self.alu_activation()
        
        if self.opcode == '000100':

            # Load from memory to store in registry operation
            # First check your cache.
            # Returns a set with index and searched address (index, address)
            cache_result = self.check_cache(result)

            if cache_result[0] is not None:
               # CacheHit. Get the value from the cache
                self.get_value_directly_from_cache(cache_result)   
            else:
                value_from_memory = self.get_value_from_memory(result)
                self.store_value_to_cache_after_ram(cache_result, value_from_memory)
                self.store_value_in_register(self.destination, value_from_memory)

        elif self.opcode == '000110':

           # First check your cache.
            # Returns a set with index and searched address (index, address)
            value_to_store = self.get_value_from_register(self.destination)
            cache_result = self.check_cache(result)

            if cache_result[0] is not None:
                # CacheHit. Store the value in the cache
                self.store_value_to_cache_directly(cache_result, value_to_store)
            else:
                # Cache Miss.
                # self.store_value_to_memory(result, value_to_store)
                self.store_value_to_cache_after_ram(cache_result, value_to_store)

        else:
            self.store_value_in_register(self.destination, result)
    

# Operations on main memory
    
    def store_value_to_memory(self, address, value_to_store):
        index = int(address, 2)
        self.ram.mem[index] = value_to_store
        action = f'store value {int(value_to_store, 2)} to memory at address {int(address, 2)}'
        self.ram.update_status(action)

        
    def get_value_from_memory(self, address):
        index = int(address, 2)
        value_get = self.ram.mem[index]
        action = f'get value {int(value_get, 2)} from memory at address {int(address, 2)}'
        self.ram.update_status(action)
        return value_get


# Operations on cache

    # This method acts on the cache in case there is a cache miss.
    # The cache_result argument is a set that contains the result of the cached check and the searched address
    def store_value_to_cache_after_ram(self, cache_result, value_to_store):

        # cache miss!
        # choose an entry to overwrite because a cache MISS occurred.
        # We use the Write-Back policy, to avoid accessing the RAM too often
        # We use directed-mapped associativity
        address = cache_result[1]
        blocks_numbers = self.cache.get_blocks_numbers()
        index_in_ram = int(address, 2)
        index_overwrite_in_cache = index_in_ram % blocks_numbers
        action = f'Cache MISS! '
        print(action, end = ' ')

        if self.cache.mem[index_overwrite_in_cache]['Dirty_Bit'] == '1':
           # The cache entry has undergone modifications so the value in RAM must first be modified and then overwritten
            address_to_modify_in_ram = self.cache.mem[index_overwrite_in_cache]['Tag']
            value_to_modify_in_ram = self.cache.mem[index_overwrite_in_cache]['Data']
            self.store_value_to_memory(address_to_modify_in_ram, value_to_modify_in_ram)


        # Overwrite in cache keeping the Dirty bit at 1 because we copied a new value for the address 
        # of reference in ram so in the future if you need to overwrite this entry it will have to be modified in ram
        self.cache.mem[index_overwrite_in_cache]['Tag'] = address
        self.cache.mem[index_overwrite_in_cache]['Data'] = value_to_store
        self.cache.mem[index_overwrite_in_cache]['Dirty_Bit'] = '1'

        # you keep track of what happens
        action = f'store value {int(value_to_store, 2)} to cache at address {index_overwrite_in_cache}'
        self.cache.update_status(action)


    
    # This method overwrites an existing value. No need access to ram just modify Dirty bit
    # The index argument is a set that contains the result of the cached check and the searched address
    def store_value_to_cache_directly(self, index, value_to_store):
        index_cache = index[0]
        # Cache Hit!
        self.cache.mem[index_cache]['Data'] = value_to_store
        action = f'Cache HIT! '
        print(action, end = ' ')
        address = self.cache.mem[index_cache]['Tag']
        if self.cache.mem[index_cache]['Dirty_Bit'] == '0':
            # Change the Dirty Bit because the value has changed compared to RAM
            self.cache.mem[index_cache]['Dirty_Bit'] = '1'
     
        # Tracks what happens
        action = f'store value {int(value_to_store, 2)} to cache at address {index_cache}'
        self.cache.update_status(action)

                
    # We get value from cache after checking existence of desired value at requested address
    # cache hit
    def get_value_directly_from_cache(self, result_check):
        index = result_check[0]
        return self.cache.mem[index]['Data']
    
    # We get value from cache after getting it from ram and saving it in cache
    # cache miss
    def get_value_from_cache_after_ram(self, result_check):
        address = result_check[1]
        value_from_ram = self.ram.mem[int(address, 2)]

        # Check if the cached index where to copy the data from RAM is free or 
        # you need to overwrite the entry and then follow the write-back policy
        blocks_numbers = self.cache.get_blocks_numbers()
        index_to_write_in_cache = int(address, 2) % blocks_numbers

        # Dirty bit check if 1 overwrite entry but first modify value in ram      
        dirty_bit = self.cache.mem[index_to_write_in_cache]['Dirty_Bit']
        if dirty_bit == '1':
            # need to update value in ram
            self.ram.mem[int(address, 2)] = self.cache.mem[index_to_write_in_cache]['Data']
        
        # overwrite cache entries
        self.cache.mem[index_to_write_in_cache]['Tag'] = address
        self.cache.mem[index_to_write_in_cache]['Data'] = value_from_ram
        self.cache.mem[index_to_write_in_cache]['Dirty_Bit'] = '0' 

        return value_from_ram



    def check_cache(self, address):
        index = 0
        # If a cache hit occurs then return the index where the entry is located 
        # and the address in ram otherwise return None and the address in ram
        for entry in self.cache.mem:
            if entry['Tag'] == address:
                # CACHE HIT!!
                return (index, address)
            index += 1
        return (None, address)



def main():
    # Testing object
    binary_code = '00000000010000010001100000000001'
    reg = REGISTERS(32)
    alu = ALU()
    test = CU(reg, alu, binary_code)
    print(test.get_value_from_memory('00111'))


