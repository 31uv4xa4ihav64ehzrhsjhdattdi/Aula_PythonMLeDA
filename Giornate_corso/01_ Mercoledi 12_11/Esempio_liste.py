    """
    Mostra varie operazioni su liste:
    creazione, aggiunta, rimozione, slicing, cicli, etc.
    """
    print("=== LISTE ===")
    # Creazione di una lista
    numeri = [1, 2, 3, 4]
    parole = ["mirko1","mirko2","mirko3"]
    misto =["mirko", 13, True, 13.23 ]
    vuota = []
    
    print("Lista Stringhe:", parole)
    print("Lista Misto:", misto)
    print("Lista iniziale:", numeri)
    
    # Aggiunta di un elemento alla fine (append)
    numeri.append(5)
    vuota.append(1)
    print("Dopo append(5):", numeri)
    
    # Inserimento in posizione specifica (insert)
    numeri.insert(2, 99)
    print("Dopo insert(2, 99):", numeri)
    
    # Rimozione di un elemento tramite valore (remove)
    numeri.remove(99)
    print("Dopo remove(99):", numeri)
    
    # Rimozione dell'ultimo elemento (pop)
    ultimo = numeri.pop()
    print(f"Dopo pop() -> elemento rimosso: {ultimo}, lista:", numeri)
    
    # Slicing
    # numeri[inizio:fine] => sotto-lista dall'indice 'inizio' fino a 'fine-1'
    print("Slicing numeri[0:2]:", numeri[0:2])
    
    # Iterazione su lista
    print("Iterazione sui valori di 'numeri':")
    for val in numeri:
        print(" -", val)
    
    # List comprehension: creiamo una lista di quadrati
    quadrati = [x*x for x in numeri]
    print("Quadrati dei numeri:", quadrati)
