# ---------------------------------------------------------
# CLASSE PRODOTTO BASE
# ---------------------------------------------------------

class Prodotto:
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita

    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione


# ---------------------------------------------------------
# CLASSI PARALLELE SENZA EREDITARIETÀ
# ---------------------------------------------------------

class Abbigliamento:
    def __init__(self, nome, costo_produzione, prezzo_vendita, materiale):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        self.materiale = materiale

    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione


class Elettronica:
    def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia_anni):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        self.garanzia_anni = garanzia_anni

    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione


# ---------------------------------------------------------
# CLASSE FABBRICA
# ---------------------------------------------------------

class Fabbrica:
    def __init__(self):
        self.inventario = {}   # {nome_prodotto : quantità}

    def aggiungi_prodotto(self, prodotto, quantita):
        nome = prodotto.nome
        if nome in self.inventario:
            self.inventario[nome] += quantita
        else:
            self.inventario[nome] = quantita

    def vendi_prodotto(self, prodotto, quantita):
        nome = prodotto.nome

        if nome not in self.inventario:
            print("Prodotto non presente in inventario.")
            return

        if self.inventario[nome] < quantita:
            print("Quantità non disponibile.")
            return

        # Rimuovo quantità venduta
        self.inventario[nome] -= quantita

        # Calcolo profitto totale
        profitto = prodotto.calcola_profitto() * quantita
        print(f"Venduti {quantita} pezzi di {nome}. Profitto: {profitto} €")

    def stato_inventario(self):
        print("\n--- Inventario ---")
        for nome, qta in self.inventario.items():
            print(f"{nome}: {qta} pezzi")
        print("------------------\n")


# ---------------------------------------------------------
# BLOCCO DI TEST
# ---------------------------------------------------------

if __name__ == "__main__":
    # Creo oggetti senza ereditarietà
    maglietta = Abbigliamento("Maglietta", 5, 15, "Cotone")
    smartphone = Elettronica("Smartphone", 120, 300, 2)

    # Creo fabbrica
    f = Fabbrica()

    # Aggiungo prodotti
    f.aggiungi_prodotto(maglietta, 50)
    f.aggiungi_prodotto(smartphone, 20)

    # Mostro stato iniziale
    f.stato_inventario()

    # Vendo
    f.vendi_prodotto(maglietta, 10)
    f.vendi_prodotto(smartphone, 5)

    # Stato finale
    f.stato_inventario()
