'''
creare una classe base Veicolo con attributi comuni a tutti i veicoli e
metodi per operazioni comuni come l'accensione e lo spegnimento. 
Derivando questa classe, creeranno specifiche classi per Auto, Furgone e Motocicletta,
aggiungendo caratteristiche uniche per ciascun tipo di veicolo.

Infine, dovranno implementare una classe GestoreParcoVeicoli per amministrare l'insieme dei veicoli.

Classe Veicolo:
    Attributi privati:
        _marca (stringa)
        _modello (stringa)
        _anno (intero)
        _accensione (booleano)
    Metodi:
        accendi(): cambia lo stato di _accensione a vero.
        spegni(): cambia lo stato di _accensione a falso.

Classi Derivate:
Auto:
    Attributi aggiuntivi come _numero_porte
    Metodo specifico come suona_clacson()
Furgone:
    Attributi per _capacità_carico
    Metodo per carica() e scarica()
Motocicletta:
    Attributo per _tipo (e.g., sportiva, touring)
    Metodo per esegui_wheelie() se il tipo è sportivo


Classe GestoreParcoVeicoli:
    Attributi:
        _veicoli: lista di tutti i veicoli.
    Metodi:
        aggiungi_veicolo(veicolo): aggiunge un veicolo alla lista.
        rimuovi_veicolo(marca, modello): rimuove un veicolo specifico dalla lista.
        lista_veicoli(): stampa un elenco di tutti i veicoli nel parco.

'''


# aggiugnere get_name a Veicolo
'''
class GestoreParcoVeicoli:

    def __init__(self, veicoli={})
        self._veicoli={}

    def aggiungi_veicolo(self, veicolo):
        self._veicoli[veicolo.get_name()] = veicolo

    def rimuovi_veicolo(self, veicolo):
        self._veicoli.pop[veicolo.get_name()] = veicolo

    def lista_veicoli(self)
'''

from abc import ABC, abstractmethod

class Veicolo(ABC): #questa è la classe astratta perchè eredita da ABC
    def __init__(self, marca, modello, anno):
        self._marca =marca  #qui incapsulamento attributi privati
        self._modello =modello
        self._anno =anno
        self._accensione =False

    #metodo per accendere il veicolo
    def accendi(self):
        self._accensione =True
        print(f"{self._marca}{self._modello} è acceso")


    #metodo per spegnere il veicolo
    def spegni(self):
        self._accensione =False
        print(f"{self._marca}{self._modello} è spento")


    #metodo astratto da implementare nelle classi derivate 
    @abstractmethod
    def get_info(self):
        print("GET INFO!!!!")

    #metodo per ottenere info di base sul veicolo
    def info_base(self):
        return f"Marca: {self.marca}, Modello {self._modello}, Anno: {self._anno}"

    #METODO EXTRA: stmpa tutte le info del veicolo
    def stampa_info(self): 
        print(self.info_base()) 
        accensione ="acceso" if self-accensione else "spento"
        print(f"Stato {accensione}")



class Auto(Veicolo):
    def __init__(self, _marca, _modello, _anno, __numero_porte):
        super().__init__(_marca, _modello, _anno)
        self.__numero_porte = __numero_porte

    def get_numero_porte(self):
        return self.__numero_porte
    
    def set_numero_porte(self,numero_porte):
        self.__numero_porte = numero_porte

    def suona_clacson(self):
        print("Beeeep")

    def get_info(self):
        Veicolo.get_info()



class Furgone(Veicolo):
    def __init__(self, _marca, _modello, _anno):
        super().__init__(_marca, _modello, _anno, )
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



class Motocicletta(Veicolo):
    def __init__(self, marca, modello, anno, tipo):
        super().__init__(marca, modello,anno)
        self.__tipo = tipo

    def esegui_wheelie(self):
        if self.__tipo.lower() == "sportivo":
            return f"Motocicletta di tipo sportiva"
        else:
            return f"Motocicletta non sportiva"
        
    def info_base(self):
        super().info_base()
        return f" Motocicletta di tipo {self.__tipo}, Marca: {self.marca}, Modello {self._modello}, Anno: {self._anno}"

        

class GestoreParcoVeicoli:

    def __init__(self, veicoli={}):
        self._veicoli={}

    def crea_veicolo(self):
        print("Inserimento nuovo veicolo: ")
        print("Seleziona il tipo di veicolo: ")
        print("a per auto;")
        print("f per furgone;")
        tipo = input("m per motocicletta: ")
        if tipo not in ["a","f","m"]:
            print("Errore: nessun tipo selezionato. ")
        else:
            marca = input("Marca: ")
            modello = input("Modello: ")
            anno = int(input("Anno: "))
            
            if tipo == "a":
                numero_porte = int(input("Numero porte: "))
                veicolo = Auto(marca, modello, anno, numero_porte)
            elif tipo == "f":
                capacita_carico = (input("Capacità carico: "))
                veicolo = Furgone(marca, modello, anno, capacita_carico)
            elif tipo == "m":
                tipologia = input("Tipologia (sportiva/touring): ")
                veicolo = Motocicletta(marca, modello, anno, tipologia)

            self.aggiungi_veicolo(veicolo)
            print("Veicolo aggiunto al parco auto. ")



    def aggiungi_veicolo(self, veicolo):
        self._veicoli[veicolo.get_name()] = veicolo

    def rimuovi_veicolo(self, veicolo):
        self._veicoli.pop[veicolo.get_name()] = veicolo

    def lista_veicoli(self):
        pass

    def start(self):
        
        attivo = True
        while attivo == True:
            print()
            print("----------------------")
            print("Sistema Gestore Veicoli")
            print("----------------------")
            print("Digita: ")
            print("i per inserire veicolo")
            print("q per uscire")
            risposta = input(": ")
            
            if risposta == "i":
                self.crea_veicolo()
            elif risposta == "q":
                attivo = False



mio_garage = GestoreParcoVeicoli()

mio_garage.start()