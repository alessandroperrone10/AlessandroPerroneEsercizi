class Automobile:
    numero_di_ruote = 4

    def __init__(self,marca,modello):
        self.marca = marca
        self.modello = modello

    def stampa_info(self):
        print("L'automobile è una ",self.marca , self.modello, self.numero_di_ruote)


auto1 = Automobile("Fiat","500")
auto2 = Automobile("Bmw","X3")

auto1.stampa_info()
auto2.stampa_info()