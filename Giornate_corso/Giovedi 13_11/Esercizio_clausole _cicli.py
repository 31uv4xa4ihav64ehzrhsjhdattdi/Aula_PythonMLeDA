# --- ESERCIZIO 1: numeri pari/dispari o stringa ---

ripeti = "si"

while ripeti == "si":

    print("Cosa vuoi inserire?")
    print("1 - Numero")
    print("2 - Stringa")
    scelta = input("Scelta: ")

    # --- PARI / DISPARI ---
    if scelta == "1":
        numero_input = input("Inserisci un numero: ")
        numero = int(numero_input)

        if numero % 2 == 0:
            print("Il numero è pari.")
        else:
            print("Il numero è dispari.")

    # --- STRINGA ---
    elif scelta == "2":
        stringa = input("Inserisci una stringa: ")
        print("Hai inserito:", stringa)

    else:
        print("Scelta non valida.")

    ripeti = input("Vuoi ripetere? (si/no): ")

print("Programma terminato.")

# --- ESERCIZIO 2: numeri primi nell'intervallo ---

ripeti = "si"

while ripeti == "si":

    inizio_input = input("Inserisci il primo numero dell'intervallo: ")
    fine_input = input("Inserisci il secondo numero dell'intervallo: ")

    inizio = int(inizio_input)
    fine = int(fine_input)

    # liste
    lista_primi = []
    lista_non_primi = []

    # ciclo sull'intervallo
    for numero in range(inizio, fine + 1):

        # verifico se è primo
        if numero > 1:
            e_primo = True

            # controllo tutti i numeri tra 2 e numero-1
            for i in range(2, numero):
                if numero % i == 0:
                    e_primo = False
                    break

            if e_primo:
                lista_primi.append(numero)
            else:
                lista_non_primi.append(numero)
        else:
            lista_non_primi.append(numero)

    print("Numeri primi:", lista_primi)
    print("Non primi:", lista_non_primi)

    ripeti = input("Vuoi ripetere? (si/no): ")

print("Programma concluso.")




