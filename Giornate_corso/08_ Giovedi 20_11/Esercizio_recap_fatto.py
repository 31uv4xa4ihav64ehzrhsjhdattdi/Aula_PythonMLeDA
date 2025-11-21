# ---------------------------------------------------------
# Classe base: Elettrodomestico
# ---------------------------------------------------------

class Elettrodomestico:
    def __init__(self, marca, modello, anno_acquisto, guasto):
        # Attributi incapsulati (privati)
        self.__marca = marca
        self.__modello = modello
        self.__anno_acquisto = anno_acquisto
        self.__guasto = guasto

    # -------- GETTER / SETTER --------
    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

    def get_modello(self):
        return self.__modello

    def set_modello(self, modello):
        self.__modello = modello

    def get_anno_acquisto(self):
        return self.__anno_acquisto

    def set_anno_acquisto(self, anno):
        if anno > 2100:
            print("Anno non valido, troppo nel futuro.")
        else:
            self.__anno_acquisto = anno

    def get_guasto(self):
        return self.__guasto

    def set_guasto(self, guasto):
        self.__guasto = guasto

    # -------- METODI LOGICI --------
    def descrizione(self):
        return f"{self.__marca} {self.__modello} (acquisto: {self.__anno_acquisto}) - Guasto: {self.__guasto}"

    def stima_costo_base(self):
        # costo generico di diagnosi/uscita tecnico
        return 30.0


# ---------------------------------------------------------
# Sottoclasse: Lavatrice
# ---------------------------------------------------------

class Lavatrice(Elettrodomestico):
    def __init__(self, marca, modello, anno_acquisto, guasto,
                 capacita_kg, giri_centrifuga):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.capacita_kg = capacita_kg
        self.giri_centrifuga = giri_centrifuga

    def stima_costo_base(self):
        # base 40€, +10 se capacità > 8kg
        costo = 40.0
        if self.capacita_kg > 8:
            costo += 10.0
        return costo


# ---------------------------------------------------------
# Sottoclasse: Frigorifero
# ---------------------------------------------------------

class Frigorifero(Elettrodomestico):
    def __init__(self, marca, modello, anno_acquisto, guasto,
                 litri, ha_freezer):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.litri = litri
        self.ha_freezer = ha_freezer

    def stima_costo_base(self):
        # base 45€, +10 se ha freezer, +5 se > 400 litri
        costo = 45.0
        if self.ha_freezer:
            costo += 10.0
        if self.litri > 400:
            costo += 5.0
        return costo


# ---------------------------------------------------------
# Sottoclasse: Forno
# ---------------------------------------------------------

class Forno(Elettrodomestico):
    def __init__(self, marca, modello, anno_acquisto, guasto,
                 tipo_alimentazione, ha_ventilato):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.tipo_alimentazione = tipo_alimentazione  # "elettrico" / "gas"
        self.ha_ventilato = ha_ventilato

    def stima_costo_base(self):
        # base 35€, +5 se elettrico, +5 se ventilato
        costo = 35.0
        if self.tipo_alimentazione.lower() == "elettrico":
            costo += 5.0
        if self.ha_ventilato:
            costo += 5.0
        return costo


# ---------------------------------------------------------
# Classe: TicketRiparazione
# ---------------------------------------------------------

class TicketRiparazione:
    def __init__(self, id_ticket, elettrodomestico):
        self.__id_ticket = id_ticket
        self.__elettrodomestico = elettrodomestico
        self.__stato = "aperto"   # "aperto", "in lavorazione", "chiuso"
        self.__note = []

    # Getter / Setter basilari
    def get_id_ticket(self):
        return self.__id_ticket

    def get_elettrodomestico(self):
        return self.__elettrodomestico

    def get_stato(self):
        return self.__stato

    def set_stato(self, nuovo_stato):
        if nuovo_stato in ("aperto", "in lavorazione", "chiuso"):
            self.__stato = nuovo_stato
        else:
            print("Stato non valido.")

    def get_note(self):
        return list(self.__note)

    def aggiungi_nota(self, testo):
        self.__note.append(testo)

    # Metodo variadico: voci extra di costo
    def calcola_preventivo(self, *voci_extra):
        base = self.__elettrodomestico.stima_costo_base()
        totale_extra = sum(voci_extra)
        return base + totale_extra

    def descrizione_breve(self):
        tipo = type(self.__elettrodomestico).__name__
        return f"[{self.__id_ticket}] {tipo} - stato: {self.__stato}"


# ---------------------------------------------------------
# Classe: Officina
# ---------------------------------------------------------

class Officina:
    def __init__(self, nome):
        self.nome = nome
        self.tickets = []

    def aggiungi_ticket(self, ticket):
        self.tickets.append(ticket)

    def chiudi_ticket(self, id_ticket):
        for t in self.tickets:
            if t.get_id_ticket() == id_ticket:
                t.set_stato("chiuso")
                return
        print(f"Ticket {id_ticket} non trovato.")

    def stampa_ticket_aperti(self):
        print(f"Ticket aperti in {self.nome}:")
        trovati = False
        for t in self.tickets:
            if t.get_stato() != "chiuso":
                print(" -", t.descrizione_breve())
                trovati = True
        if not trovati:
            print(" Nessun ticket aperto.")

    def totale_preventivi(self):
        totale = 0.0
        for t in self.tickets:
            # esempio: nessuna extra, solo costo base
            totale += t.calcola_preventivo()
        return totale

    def statistiche_per_tipo(self):
        """
        Usa type() per contare quanti ticket ci sono
        per Lavatrice, Frigorifero e Forno.
        """
        cont_lav = 0
        cont_frig = 0
        cont_forno = 0

        for t in self.tickets:
            elettro = t.get_elettrodomestico()
            # uso esplicito di type() come da consegna
            if type(elettro) is Lavatrice:
                cont_lav += 1
            elif type(elettro) is Frigorifero:
                cont_frig += 1
            elif type(elettro) is Forno:
                cont_forno += 1

        print("\nStatistiche per tipo di elettrodomestico:")
        print(" - Lavatrici in riparazione:", cont_lav)
        print(" - Frigoriferi in riparazione:", cont_frig)
        print(" - Forni in riparazione:", cont_forno)


# ---------------------------------------------------------
# ESEMPIO D'USO (main didattico)
# ---------------------------------------------------------

if __name__ == "__main__":
    # Creo alcuni elettrodomestici
    lav1 = Lavatrice("Bosch", "Serie 6", 2019, "Non centrifuga", 9, 1400)
    lav2 = Lavatrice("Whirlpool", "Eco", 2015, "Perde acqua", 7, 1200)

    frigo1 = Frigorifero("Samsung", "CoolPlus", 2020, "Non raffredda", 430, True)
    frigo2 = Frigorifero("LG", "SmartFridge", 2022, "Rumore strano", 350, False)

    forno1 = Forno("Candy", "FornoX", 2018, "Non si accende", "elettrico", True)

    # Creo ticket con voci extra diverse
    t1 = TicketRiparazione("T1", lav1)
    t2 = TicketRiparazione("T2", lav2)
    t3 = TicketRiparazione("T3", frigo1)
    t4 = TicketRiparazione("T4", frigo2)
    t5 = TicketRiparazione("T5", forno1)

    # Aggiungo qualche nota
    t1.aggiungi_nota("Cliente lamenta odore bruciato.")
    t3.aggiungi_nota("Possibile perdita di gas.")

    # Creo l'officina e aggiungo i ticket
    off = Officina("Officina ElettroFix")
    off.aggiungi_ticket(t1)
    off.aggiungi_ticket(t2)
    off.aggiungi_ticket(t3)
    off.aggiungi_ticket(t4)
    off.aggiungi_ticket(t5)

    # Stampa dei ticket aperti
    off.stampa_ticket_aperti()

    # Calcolo di un preventivo con extra variadici (pezzi + manodopera)
    preventivo_t1 = t1.calcola_preventivo(25.0, 40.0)  # 25 pezzi, 40 manodopera
    print(f"\nPreventivo ticket T1: {preventivo_t1} €")

    # Chiudo un ticket
    off.chiudi_ticket("T2")

    # Ristampa ticket aperti
    print()
    off.stampa_ticket_aperti()

    # Totale preventivi (solo base)
    totale = off.totale_preventivi()
    print(f"\nTotale dei preventivi (solo costo base): {totale} €")

    # Statistiche per tipo (uso type())
    off.statistiche_per_tipo()
