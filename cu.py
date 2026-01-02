# This is a simulation of the CU component of a MIPS32 architecture cpu

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

# for testing
from registers import REGISTERS
from alu import ALU

class CU:
    def __init__(self, registers_object, alu_object, cache_object, binary_code):
        self.binary_code = binary_code
        self.opcode = ''
        self.source_one = ''
        self.source_two = ''
        self.destination = ''
        self.alu = alu_object
        self.registers = registers_object
        self.cache = cache_object
        self.ram = RAM(32)
        


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
            # This is TypeI instruction case
            # source_one = rs source_two = immd destination = rt
            self.source_one = self.binary_code[6:11]
            self.destination = self.binary_code[11:16]
            # This is an immediate value
            self.source_two = self.binary_code[16:]

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
        value_two = self.get_value_from_register(self.source_two)

        # Activate the alu to perform the calculations
        result = self.alu.get_opcode_and_values_from_cu(self.opcode, value_one, value_two)
        return result

    
    def execute_binary_code(self):
        # valutare l'opcode per capire come gestire i risultati della alu
        result = self.alu_activation()
        
        if self.opcode == '000100':

            # Load from memory to store in registry operation
            # Per prima cosa controllare la cache.
            # Ritorna un set con indice e indirizzo cercato (index, address)
            cache_result = self.check_cache(result)

            if cache_result[0] is not None:
                # Cache Hit. Prendere il valore dalla cache
                ...   
            else:
                value_from_memory = self.get_value_from_memory(result)
                self.store_value_in_register(self.destination, value_from_memory)

        elif self.opcode == '000110':

            # Per prima cosa controllare la cache.
            # Ritorna un set con indice e indirizzo cercato (index, address)
            value_to_store = self.get_value_from_register(self.destination)
            cache_result = self.check_cache(result)

            if cache_result[0] is not None:
                # Cache Hit. Conserva il valore nella cache
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

    # Questo metodo agisce sulla cache in caso ci cache Miss.
    # L'argomento index è un set che contiene il risultato del controllo in cache e l'indirizzo cercato
    def store_value_to_cache_after_ram(self, index, value_to_store):

        # cache miss!
        # scegliere un entry da sovrascrivere perché si è verificato un cache MISS.
        # Adoperiamo la policy Write-Back, per evitare di accedere troppo spesso alla ram
        # Adoperiamo la associatività directed-mapped
        address = index[1]
        blocks_numbers = self.cache.get_blocks_numbers()
        #print(blocks_numbers)
        index_in_ram = int(address, 2)
        #print(index_in_ram)
        #print(2%32)
        index_overwrite_in_cache = index_in_ram % blocks_numbers
        action = f'Cache MISS! '
        print(action, end = ' ')

        if self.cache.mem[index_overwrite_in_cache]['Dirty_Bit'] == '1':
            # L'entry in cache ha subito modifiche quindi va prima modificato il valore in ram e poi sovrascritto
            address_to_modify_in_ram = self.cache.mem[index_overwrite_in_cache]['Tag']
            value_to_modify_in_ram = self.cache.mem[index_overwrite_in_cache]['Data']
            self.store_value_to_memory(address_to_modify_in_ram, value_to_modify_in_ram)


        # Sovrascrivere in cache mantenento il Dirty bit ad 1 perchè abbiamo copiato un valore nuovo per l'indirizzo 
        # di riferimento in ram quindi in furuto se bisogna sovrascrivere questo entry andrà modificato in ram
        self.cache.mem[index_overwrite_in_cache]['Tag'] = address
        self.cache.mem[index_overwrite_in_cache]['Data'] = value_to_store
        self.cache.mem[index_overwrite_in_cache]['Dirty_bit'] = '1'

        # si tiene traccia di ciò che accade
        action = f'store value {int(value_to_store, 2)} to cache at address {index_overwrite_in_cache}'
        self.cache.update_status(action)


    
    # This method overwrites an existing value. No need access to ram just modify Dirty bit
    # L'argomento index è un set che contiene il risultato del controllo in cache e l'indirizzo cercato
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
     
        # si tiene traccia di ciò che accade
        action = f'store value {int(value_to_store, 2)} to cache at address {index_cache}'
        self.cache.update_status(action)

                
    # Prendiamo valore dalla cache dopo controllo di esistenza del valore desiderato all'indirizzo richiesto
    # cache hit
    def get_value_directly_from_cache(self, result_check):
        index = result_check[0]
        return self.cache.mem[index]['Data']
    
    # Prendiamo valore dalla cache dopo averlo preso dalla ram e salvato in cache
    # cache miss
    def get_value_from_cache_after_ram(self, result_check):
        address = result_check[1]
        value_from_ram = self.ram.mem[int(address, 2)]

        # Verificare se nell'indice in cache dove copiare il dato dalla ram è libero oppure 
        # bisogna sovrascrivere l'entry e quindi seguire la policy di write-back
        blocks_numbers = self.cache.get_blocks_numbers()
        index_to_write_in_cache = int(address, 2) % blocks_numbers

        # Controllo Dirty bit se 1 sovrascrivere entry ma prima modificare valore in ram     
        dirty_bit = self.cache.mem[index_to_write_in_cache]['Dirty_Bit']
        if dirty_bit == '1':
            # bisogna aggiornare valore in ram
            self.ram.mem[int(address, 2)] = self.cache.mem[index_to_write_in_cache]['Data']
        
        # sovrascrivere entry in cache
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


