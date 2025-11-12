# ---------------------------------------------------------
# Esercizio: Simulatore di login base in Python
# Requisiti: usare solo if, variabili, liste e operatori logici
# ---------------------------------------------------------

# Dati hardcoded (credenziali corrette)
username_corretti = ["admin"]
password_corretti = ["12345"]

# Input dell'utente
nome = input("Inserisci il nome utente: ")
password = input("Inserisci la password: ")

# Verifica delle credenziali
if nome == username_corretti[0] and password == password_corretti[0]:
    print("Accesso consentito! Benvenuto,", nome)

    # Domande aggiuntive dopo il login
    print("\nOra scegli una delle seguenti domande:")
    print("1. Qual è il tuo colore preferito?")
    print("2. Qual è il tuo animale preferito?")

    scelta = input("Scrivi 1 o 2: ")

    if scelta == "1":
        colore = input("Inserisci il tuo colore preferito: ")
        print("Hai scelto il colore:", colore)
    elif scelta == "2":
        animale = input("Inserisci il tuo animale preferito: ")
        print("Hai scelto l'animale:", animale)
    else:
        print("Scelta non valida.")
else:
    print("Accesso negato! Nome utente o password errati.")
