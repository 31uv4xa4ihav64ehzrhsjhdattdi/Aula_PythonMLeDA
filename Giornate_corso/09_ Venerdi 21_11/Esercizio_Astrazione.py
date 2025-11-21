from abc import ABC, abstractmethod

# ---------------------------------------------------------
# Classe astratta: VeicoloTrasporto
# ---------------------------------------------------------

class VeicoloTrasporto(ABC):
    def __init__(self, targa: str, peso_massimo: int):
        self._targa = targa
        self._peso_massimo = peso_massimo
        self._carico_attuale = 0

    # metodi concreti comuni
    def carica(self, peso: int):
        if peso < 0:
            print("Non puoi caricare un peso negativo.")
            return

        if self._carico_attuale + peso <= self._peso_massimo:
            self._carico_attuale += peso
            print(f"[{self._targa}] Caricati {peso} kg. Carico attuale: {self._carico_attuale} kg.")
        else:
            print(f"[{self._targa}] PESO ECCESSIVO: supereresti la capacità massima di {self._peso_massimo} kg.")

    def scarica(self):
        print(f"[{self._targa}] Scaricati {self._carico_attuale} kg. Carico riportato a 0.")
        self._carico_attuale = 0

    @abstractmethod
    def costo_manutenzione(self) -> float:
        """Metodo astratto: ogni veicolo ha la sua regola di manutenzione."""
        pass

    def descrizione(self) -> str:
        return f"{self.__class__.__name__} [{self._targa}] - max {self._peso_massimo} kg, carico {self._carico_attuale} kg"


# ---------------------------------------------------------
# Sottoclasse: Camion
# Regola: 100 € per asse + 1 € per kg di carico massimo
# ---------------------------------------------------------

class Camion(VeicoloTrasporto):
    def __init__(self, targa: str, peso_massimo: int, numero_assi: int):
        super().__init__(targa, peso_massimo)
        self.numero_assi = numero_assi

    def costo_manutenzione(self) -> float:
        return 100 * self.numero_assi + 1 * self._peso_massimo


# ---------------------------------------------------------
# Sottoclasse: Furgone
# Regola: elettrico = 200 €, diesel = 150 €
# ---------------------------------------------------------

class Furgone(VeicoloTrasporto):
    def __init__(self, targa: str, peso_massimo: int, alimentazione: str):
        super().__init__(targa, peso_massimo)
        self.alimentazione = alimentazione.lower()  # "diesel" / "elettrico"

    def costo_manutenzione(self) -> float:
        if self.alimentazione == "elettrico":
            return 200.0
        else:
            return 150.0


# ---------------------------------------------------------
# Sottoclasse: Motocarro
# Regola: 50 € per ogni anno di servizio
# ---------------------------------------------------------

class Motocarro(VeicoloTrasporto):
    def __init__(self, targa: str, peso_massimo: int, anni_servizio: int):
        super().__init__(targa, peso_massimo)
        self.anni_servizio = anni_servizio

    def costo_manutenzione(self) -> float:
        return 50.0 * self.anni_servizio


# ---------------------------------------------------------
# Gestore flotta
# ---------------------------------------------------------

class GestoreFlotta:
    def __init__(self, nome: str):
        self.nome = nome
        self.veicoli: list[VeicoloTrasporto] = []

    def aggiungi_veicolo(self, veicolo: VeicoloTrasporto):
        self.veicoli.append(veicolo)

    def rimuovi_veicolo(self, targa: str):
        for v in self.veicoli:
            if v._targa == targa:
                self.veicoli.remove(v)
                print(f"Veicolo {targa} rimosso dalla flotta.")
                return
        print(f"Nessun veicolo trovato con targa {targa}.")

    def costo_totale_manutenzione(self) -> float:
        totale = 0.0
        for v in self.veicoli:
            totale += v.costo_manutenzione()  # polimorfismo
        return totale

    def stampa_veicoli(self):
        print(f"Flotta di {self.nome}:")
        if not self.veicoli:
            print("  Nessun veicolo presente.")
            return
        for v in self.veicoli:
            print("  -", v.descrizione(),
                  "| Costo manutenzione:", v.costo_manutenzione(), "€")


# ---------------------------------------------------------
# Esempio d'uso (main)
# ---------------------------------------------------------

if __name__ == "__main__":
    # creo alcuni veicoli
    c1 = Camion("AB123CD", 12000, 4)
    c2 = Camion("EF456GH", 18000, 5)

    f1 = Furgone("FI111AA", 3500, "diesel")
    f2 = Furgone("FI222BB", 3000, "elettrico")

    m1 = Motocarro("MC999ZZ", 1500, 6)

    # creo la flotta
    flotta = GestoreFlotta("TransLogistica")

    flotta.aggiungi_veicolo(c1)
    flotta.aggiungi_veicolo(c2)
    flotta.aggiungi_veicolo(f1)
    flotta.aggiungi_veicolo(f2)
    flotta.aggiungi_veicolo(m1)

    # qualche operazione di carico/scarico
    c1.carica(5000)
    c1.carica(8000)   # prova superamento peso
    c1.scarica()

    f2.carica(1000)

    # stampa veicoli e costi
    flotta.stampa_veicoli()

    print("\nCosto totale di manutenzione della flotta:",
          flotta.costo_totale_manutenzione(), "€")
