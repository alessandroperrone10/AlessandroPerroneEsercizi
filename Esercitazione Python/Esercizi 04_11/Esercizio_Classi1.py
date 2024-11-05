class Punto:
    def __init__(self, x):
        self.x = x
    
    def stampa_punto(self):
        print("Il punto inserito è: ",self.x)

    def modifica_punto(self):
        dx = float(input("Inserisci il punto x da modificare: "))
        self.x = dx
        self.stampa_punto()

    def distanza_origine(self):
        distanza = (self.x ** 2) ** 0.5
        print("La distanza dall'origine dei due punti è: ", distanza)


class PianoCartesiano:
    def __init__(self):
        self.piano_cartesiano = []

    def aggiungi_punto(self,punto):
        self.piano_cartesiano.append(Punto(punto))


    def stampa_piano(self):
       print("Punti nel piano cartesiano:")
       for punto in self.piano_cartesiano:
           punto.stampa_punto()
        
    


primo_punto = float(input("Inserisci il punto x: "))

coordinata1 = Punto(primo_punto)

coordinata1.stampa_punto()

domanda = input("Vuoi creare un piano cartesiano? si/no: ")

if domanda == "si":
    secondo_punto = float(input("Inserisci il secondo punto: "))
    piano = PianoCartesiano()
    piano.aggiungi_punto(primo_punto)
    piano.aggiungi_punto(secondo_punto)
    piano.stampa_piano()
else:
    modifica = input("Vuoi modificare le coordinate?: si o no? Scrivi distanza per vedere la distanza dall'origine: ")
    if modifica == "si":
        coordinata1.modifica_punto()
    elif modifica == "distanza":
        coordinata1.distanza_origine()


