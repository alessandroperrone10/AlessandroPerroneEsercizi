class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def stampa_punti(self):
        print("I due nuovi punti sono: ",self.x, " " ,self.y)


    def modifica_punti(self):
        dx = float(input("Inserisci il punto x da modificare: "))
        dy = float(input("Inserisci il punto y da modificare: "))

        coordinate.x = dx
        coordinate.y = dy

        coordinate.stampa_punti()

    def distanza_origine(self):
        distanza = (self.x ** 2 + self.y ** 2) ** 0.5
        print("La distanza dall'origine dei due punti è: ", distanza)



primo_punto = float(input("Inserisci il punto x: "))
secondo_punto = float(input("Inserisci il punto y: "))

coordinate = Punto(primo_punto,secondo_punto)

coordinate.stampa_punti()


modifica = input("Vuoi modificare le coordinate?: si o no? Scrivi distanza per vedere la distanza dall'origine: ")

if modifica == "si":
    coordinate.modifica_punti()
elif modifica == "distanza":
    coordinate.distanza_origine()