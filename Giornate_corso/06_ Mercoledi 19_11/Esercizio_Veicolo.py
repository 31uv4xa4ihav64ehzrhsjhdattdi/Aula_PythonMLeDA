# ---------------------------------------------------------
# Classe base: Veicolo
# ---------------------------------------------------------

class Veicolo:
    def __init__(self, marca, modello, anno):
        # Attributi "privati" (incapsulamento)
        self.__marca = marca
        self.__modello = modello
        self.__anno = anno
        self.__accensione = False

    # Getter (se servono all'esterno)
    def get_marca(self):
        return self.__marca

    def get_modello(self):
        return self.__modello

    def get_anno(self):
        return self.__anno

    def is_acceso(self):
        return self.__accensione

    # Metodi richiesti
    def accendi(self):
        self.__accensione = True

    def spegni(self):
        self.__accensione = False

    def descrizione_base(self):
        stato = "acceso" if self.__accensione else "spento"
        return f"{self.__marca} {self.__modello} ({self.__anno}) - {stato}"


# ---------------------------------------------------------
# Classi derivate
# ---------------------------------------------------------

class Auto(Veicolo):
    def __init__(self, marca, modello, anno, numero_porte):
        super().__init__(marca, modello, anno)
        self.numero_porte = numero_porte

    def suona_clacson(self):
        print("Clacson: BEEEEEP!")

    def __str__(self):
        return f"Auto: {self.descrizione_base()}, porte: {self.numero_porte}"


class Furgone(Veicolo):
    def __init__(self, marca, modello, anno, capacita_carico):
        super().__init__(marca, modello, anno)
        self.capacita_carico = capacita_carico  # in kg
        self.carico_attuale = 0

    def carica(self, peso):
        if self.carico_attuale + peso <= self.capacita_carico:
            self.carico_attuale += peso
            print(f"Caricati {peso} kg. Carico attuale: {self.carico_attuale} kg")
        else:
            print("Impossibile caricare: supereresti la capacità massima.")

    def scarica(self, peso):
        if peso <= self.carico_attuale:
            self.carico_attuale -= peso
            print(f"Scaricati {peso} kg. Carico attuale: {self.carico_attuale} kg")
        else:
            print("Non puoi scaricare più di quanto hai caricato.")

    def __str__(self):
        return (f"Furgone: {self.descrizione_base()}, "
                f"capacità: {self.capacita_carico} kg, "
                f"carico attuale: {self.carico_attuale} kg")


class Motocicletta(Veicolo):
    def __init__(self, marca, modello, anno, tipo):
        super().__init__(marca, modello, anno)
        self.tipo = tipo  # es. "sportiva", "touring", ecc.

    def esegui_wheelie(self):
        if self.tipo.lower() == "sportiva":
            print("La moto impenna! (wheelie)")
        else:
            print("Questa moto non è adatta per fare wheelie in sicurezza.")

    def __str__(self):
        return f"Motocicletta: {self.descrizione_base()}, tipo: {self.tipo}"


# ---------------------------------------------------------
# Classe GestoreParcoVeicoli
# ---------------------------------------------------------

class GestoreParcoVeicoli:
    def __init__(self):
        self.veicoli = []  # lista di tutti i veicoli

    def aggiungi_veicolo(self, veicolo):
        self.veicoli.append(veicolo)

    def rimuovi_veicolo(self, marca, modello):
        for v in self.veicoli:
            if v.get_marca() == marca and v.get_modello() == modello:
                self.veicoli.remove(v)
                print(f"Veicolo {marca} {modello} rimosso dal parco.")
                return
        print(f"Nessun veicolo trovato con marca {marca} e modello {modello}.")

    def lista_veicoli(self):
        if not self.veicoli:
            print("Nessun veicolo nel parco.")
        else:
            print("Veicoli presenti nel parco:")
            for v in self.veicoli:
                print(" -", v)


# ---------------------------------------------------------
# Esempio d'uso (demo)
# ---------------------------------------------------------

if __name__ == "__main__":
    # Creo alcuni veicoli
    auto1 = Auto("Fiat", "Panda", 2018, 5)
    furgone1 = Furgone("Iveco", "Daily", 2020, 3000)
    moto1 = Motocicletta("Yamaha", "R6", 2019, "sportiva")

    # Accendo i veicoli per vedere il cambio di stato
    auto1.accendi()
    moto1.accendi()

    # Creo gestore parco
    gestore = GestoreParcoVeicoli()

    # Aggiungo veicoli
    gestore.aggiungi_veicolo(auto1)
    gestore.aggiungi_veicolo(furgone1)
    gestore.aggiungi_veicolo(moto1)

    # Mostro lista
    gestore.lista_veicoli()

    # Provo qualche metodo specifico
    auto1.suona_clacson()
    furgone1.carica(500)
    furgone1.scarica(200)
    moto1.esegui_wheelie()

    # Rimuovo un veicolo
    gestore.rimuovi_veicolo("Fiat", "Panda")
    gestore.lista_veicoli()
