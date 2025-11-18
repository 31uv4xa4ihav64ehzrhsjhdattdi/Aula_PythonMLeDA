# ---------------------------------------------------------
# Esercizio: Libreria con classi Libro e Libreria
# ---------------------------------------------------------

class Libro:
    def __init__(self, titolo, autore, isbn):
        self.titolo = titolo
        self.autore = autore
        self.isbn = isbn

    def descrizione(self):
        return f"Titolo: {self.titolo}, Autore: {self.autore}, ISBN: {self.isbn}"


class Libreria:
    def __init__(self):
        # catalogo è una lista di oggetti Libro
        self.catalogo = []

    def aggiungi_libro(self, libro):
        self.catalogo.append(libro)

    def rimuovi_libro(self, isbn):
        # rimuove il primo libro che ha quell'ISBN
        for libro in self.catalogo:
            if libro.isbn == isbn:
                self.catalogo.remove(libro)
                print(f"Libro con ISBN {isbn} rimosso.")
                return
        print(f"Nessun libro trovato con ISBN {isbn}.")

    def cerca_per_titolo(self, titolo):
        # restituisce una lista di libri che hanno quel titolo
        risultati = []
        for libro in self.catalogo:
            if libro.titolo == titolo:
                risultati.append(libro)
        return risultati

    def mostra_catalogo(self):
        if not self.catalogo:
            print("Il catalogo è vuoto.")
        else:
            print("Catalogo libri:")
            for libro in self.catalogo:
                print(" -", libro.descrizione())


# ---------------------------------------------------------
# Esempio d'uso 
# ---------------------------------------------------------
if __name__ == "__main__":
    # Creo alcuni libri
    libro1 = Libro("1984", "George Orwell", "111")
    libro2 = Libro("Il Signore degli Anelli", "J.R.R. Tolkien", "222")
    libro3 = Libro("1984", "George Orwell", "333")

    # Creo la libreria
    libreria = Libreria()

    # Aggiungo libri
    libreria.aggiungi_libro(libro1)
    libreria.aggiungi_libro(libro2)
    libreria.aggiungi_libro(libro3)

    # Mostro catalogo
    libreria.mostra_catalogo()

    # Cerco per titolo
    print("\nRisultati ricerca per titolo '1984':")
    risultati = libreria.cerca_per_titolo("1984")
    for libro in risultati:
        print(" *", libro.descrizione())

    # Rimuovo un libro per ISBN
    libreria.rimuovi_libro("222")

    # Catalogo finale
    print("\nDopo la rimozione:")
    libreria.mostra_catalogo()
