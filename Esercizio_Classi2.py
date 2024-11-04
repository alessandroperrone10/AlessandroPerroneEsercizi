class Libro:

    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
        
    def descrizione(self):
        print("Il libro", self.titolo, "è stato scritto da", self.autore, "e ha", self.pagine, "pagine")

class Biblioteca:

    def __init__(self):
        self.libri = []

    def aggiungi_libro(self, titolo, autore, pagine):
        libro = Libro(titolo, autore, pagine)
        self.libri.append(libro)
        print("Il libro è stato aggiunto.")

    def stampa_libri(self):
        for libro in self.libri:
            libro.descrizione()


biblioteca = Biblioteca()

while True:
    titolo = input("Inserisci il titolo del libro: ")
    autore = input("Inserisci l'autore del libro: ")
    pagine = input("Inserisci il numero di pagine del libro: ")

    biblioteca.aggiungi_libro(titolo, autore, pagine)

    continuare = input("Vuoi inserire un altro libro? (si o no): ").lower()
    if continuare == "no":
        break


biblioteca.stampa_libri()


# libro = Libro(titolo,autore,pagine)

# libro.descrizione()