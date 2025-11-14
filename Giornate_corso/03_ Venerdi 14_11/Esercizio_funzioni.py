import random

def indovina_numero():
    # genera numero casuale tra 1 e 100
    segreto = random.randint(1, 100)
    print("Ho pensato a un numero tra 1 e 100.")
    print("Prova a indovinarlo! (scrivi 'esci' per terminare)")

    while True:
        tentativo = input("Inserisci un numero: ")

        if tentativo == "esci":
            print("Hai deciso di uscire. Il numero era:", segreto)
            break

        tentativo = int(tentativo)

        if tentativo == segreto:
            print("Bravo! Hai indovinato il numero:", segreto)
            break
        elif tentativo < segreto:
            print("Il numero da indovinare è PIÙ ALTO.")
        else:
            print("Il numero da indovinare è PIÙ BASSO.")

# avvio gioco
indovina_numero()




#------------------------------------------------------------

def fibonacci_fino_a_n():
    n = int(input("Inserisci un numero N: "))

    # primi due numeri di Fibonacci
    a = 0
    b = 1

    print("Sequenza di Fibonacci fino a", n, ":")

    while a <= n:
        print(a)
        # passo successivo: nuovo numero è somma dei due precedenti
        prossimo = a + b
        a = b
        b = prossimo

# avvio funzione
fibonacci_fino_a_n()

