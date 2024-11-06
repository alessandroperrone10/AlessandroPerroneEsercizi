class Auto(Veicolo):
    def __init__(self, _marca, _modello, _anno, _accensione,_numero_porte):
        super().__init__(_marca, _modello, _anno, _accensione)
        self.__numero_porte = __numero_porte

    def get_numero_porte(self):
        return self.__numero_porte
    
    def set_numero_porte(self,numero_porte):
        self.__numero_porte = numero_porte

    def suona_clacson(self):
        print("Beeeep")






class Furgone(Veicolo):
    def __init__(self, _marca, _modello, _anno, _accensione,_capacita_carico):
        super().__init__(_marca, _modello, _anno, _accensione)
        self._capacita_carico = False

    def get_capacita_carico(self):
        return self._capacita_carico
    
    def set_capacita_carico(self,capacita_carico):
        self._capacita_carico = capacita_carico

    def carica(self):
        if self._capacita_carico == False:
            self._capacita_carico == True
            print("Ho caricato il furgone")
        else:
            print("Il furgone è già pieno")

    def scarica(self):
        if self._capacita_carico == True:
            self._capacita_carico == False
            print("Ho scaricato il furgone")
        else:
            print("Il furgone è già vuoto")




auto = Auto("Bmw","Serie2",2024,False,4)