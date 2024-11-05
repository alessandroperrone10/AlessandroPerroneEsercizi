
##Ereditarietà singola
class Veicolo:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello

    def mostra_informazioni(self):
        print(f"Veicolo marca {self.marca}, modello {self.modello}")

class DotazioniSpeciali:
    def __init__(self, dotazioni):
        self.dotazioni = dotazioni

    def mostra_dotazioni(self):
        print(f"Dotazioni speciali: {', '.join(self.dotazioni)}")


class Quad(Veicolo):
    pass


class AutomobileSportiva(Veicolo, DotazioniSpeciali):
    def __init__(self, marca, modello, dotazioni, cavalli):
        Veicolo.__init__(self, marca, modello)
        #Alternbatica a super per l'ereditarietà multipla
        DotazioniSpeciali.__init__(self, dotazioni)
        self.cavalli = cavalli
    
    def mostra_dotazioni(self):
         super().mostra_informazioni()
         #Chiamiamo il metodo della prima superclasse
         print(f"Potenza: {self.cavalli} CV")
         self.mostra_dotazioni()
         #Possiamo chiamare metosi di entrambe le superclassi



auto_sportiva = AutomobileSportiva("Ferrari", "F8", "Abs", 720)

#auto_sportiva.mostra_informazioni()

auto_sportiva.mostra_dotazioni()