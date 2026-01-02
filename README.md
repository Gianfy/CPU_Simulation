# CPU_Simulation

Simulazione molto semplice del comportamento di una CPU (del tipo MIPS32).
Il progetto volutamente semplificato serve a mostrare il ciclo di istruzione del processore (fetch, decode, execute), l'interazione tra i vari componenti interni e le memorie (cu, alu, registri, cache, ram) e alcuni esempi di istruzioni in codice binario.

## Stato attuale
- Implementazione: add, sub, mul, load (da Ram a registro), store (da registro a Ram) tramite la cache.
- Mancano jump e altre istruzioni di controllo di flusso; miglior gestione dei formati e dei tipi.
- Per quanto riguarda la Cache è ampliata la Directed-Mapped per l'associatività e Write-back per la write policy.È possibile implementare le altre policy in futuro.

## Requisiti
- Python 3.8+ (nessuna dipendenza esterna).

## Uso rapido
1. Posizionati nella root del repository (dove c'è 'simulation.py')
2. Esegui:
    ...
    python3 simulation.py input.txt
    ...

    Dove 'input.txt' è il file con le istruzioni in formato binario.

## Formato del file di input
- Ogni riga contiene una istruzione in codice binario (stringa in 32 bit) secondo un formato MIPS32:
    - type R op 00000 rs 00000 rt 00000 rd 00000 shamt 00000 FUNC 000000
    - type I op 000000 rs 00000 rt 00000 imd 0000000000000000     rt destination
    - type J op 000000 rs 00000 rt 00000 offset 0000000000000000  rt destination( o source in SW)
    - Il file input mostra un esempio di formato di test.vuole simulare un eventuale file in formato assembly che ipoteticamente fosse trasformato in binario riga per riga e che per il momento viene direttamente eseguito istruzione per istruzione.(si implementerà la possibilità di caricarlo in ram da cui poi avverebbe la lettura similmente alla realtà).

## Output
- Il programma stampa in console i log delle operazioni che sta compiendo sulle memorie, i registri, le fasi in cache e accesso alla lau. (tutti i dati sono in formato intero per essere un pò più leggibili)

    Esempio:

    Decoding the instruction 00010000000000010000000000001010 : 
    Opcode: 000100, soure_one: 00000, source_two: 0000000000001010, destination: 00001

    Access to Registers: get value 0 from register at address 0
    Activation ALU: add value 10 with value 0. Result is the memory address 10
    Access to Main Memory: get value 25 from memory at address 10
    Cache MISS!  Access to Cache: store value 25 to cache at address 10
    Access to Registers: store value 25 in register at address 1

## Scelte di implementazione
- È stato scelto per provare ad avvicinarsi un pochino alla relatà di utilizzare il tipo stringa per la rappresentazione dei dati in formato binario ('0b00' oppure '00').
- La manipolazione nelle operazioni avviene con la trasformazione in interi per indicare i valori numerici e quindi gli indici di memoria nelle strutture dati.
- Per le operazioni di load e store i dati devono sempre essere rappresentati come binari in forma di tstringhe.
- La struttura dati usata per le memorie è la lista mentre per la cache è una lista di dizionari ([{'Tag': , 'Data': , 'Dirty_Bit'}])

## TEntativi di implementazioni futuri
- Aggiungere  nuove istruzioni.
- Implementare il caricamento del file di istruzioni in memoria principale. (più vicino alla realtà).

## Come contribuire
- Sarei contento che ci fossero correzioni e miglioramenti da parte di chi è più esperto anche proponendo uno stravolgimento della logica generale se (come è presumibile) si riscontra che la mia logica è troppo grezza e poco funzionale.
- Grazie per il vostro aiuto e volonta di educarmi a fare meglio.

## Licenza
- Progetto di studio e di apprendimento