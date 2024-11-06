'''
creare una classe base Veicolo con attributi comuni a tutti i veicoli e
metodi per operazioni comuni come l'accensione e lo spegnimento. 
Derivando questa classe, creeranno specifiche classi per Auto, Furgone e Motocicletta,
aggiungendo caratteristiche uniche per ciascun tipo di veicolo.

Infine, dovranno implementare una classe GestoreParcoVeicoli per amministrare l'insieme dei veicoli.

Classe Veicolo:
    Attributi privati:
        __marca (stringa)
        __modello (stringa)
        __anno (intero)
        __accensione (booleano)
    Metodi:
        accendi(): cambia lo stato di __accensione a vero.
        spegni(): cambia lo stato di __accensione a falso.

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
        __veicoli: lista di tutti i veicoli.
    Metodi:
        aggiungi_veicolo(veicolo): aggiunge un veicolo alla lista.
        rimuovi_veicolo(marca, modello): rimuove un veicolo specifico dalla lista.
        lista__veicoli(): stampa un elenco di tutti i veicoli nel parco.

'''


from abc import ABC, abstractmethod

class Veicolo(ABC): #questa è la classe astratta perchè eredita da ABC, 
    #non si possono creare istanze direttamente di questa classe, ma deve essere usata come base per altre classi
    def __init__(self, marca, modello, anno):
        self.__marca =marca  #qui incapsulamento attributi privati
        self.__modello =modello
        self.__anno =anno
        self.__accensione =False

    #metodo per accendere il veicolo
    def accendi(self):
        self.__accensione =True
        print(f"{self.__marca}{self.__modello} è acceso")

    #metodo per spegnere il veicolo
    def spegni(self):
        self.__accensione =False
        print(f"{self.__marca}{self.__modello} è spento")


    #metodo per ottenere info di base sul veicolo
    @abstractmethod
    def info_base(self):
        return f"Marca: {self.__marca}, Modello {self.__modello}, Anno: {self.__anno}"

    #METODO EXTRA: stmpa tutte le info del veicolo
    def stampa_info(self): 
        print(self.info_base()) 
        accensione ="acceso" if self-accensione else "spento"
        print(f"Stato {accensione}")

    def get_marca(self):
        return self.__marca

    def get_modello(self):
        return self.__modello

    def get_anno(self):
        return self.__anno

    def get_accensione(self):
        return self.__accensione

class Auto(Veicolo):
    def __init__(self, __marca, __modello, __anno, __numero_porte):
        super().__init__(__marca, __modello, __anno)
        self.__numero_porte = __numero_porte

    def get_numero_porte(self):
        return self.__numero_porte
    
    def set_numero_porte(self,numero_porte):
        self.__numero_porte = numero_porte

    def suona_clacson(self):
        print("Beeeep")


    def info_base(self):
        return super().info_base()+f" Auto a {self.get_numero_porte()} porte."



class Furgone(Veicolo):
    def __init__(self, __marca, __modello, __anno):
        super().__init__(__marca, __modello, __anno)
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

    def info_base(self):
        if self.get_capacita_carico() == True:
            return super().info_base()+", Furgone carico"
        else:
            return super().info_base()+", Furgone scarico"

class Motocicletta(Veicolo):
    def __init__(self, marca, modello, anno, tipo):
        super().__init__(marca, modello,anno)
        self.__tipo = tipo

    def esegui_wheelie(self):
        if self.__tipo.lower() == "sportivo":
            return f"Motocicletta di tipo sportiva"
        else:
            return f"Motocicletta non sportiva"
    
    def get_tipo(self):
        return self.__tipo
    
    def info_base(self):
        return super().info_base()+f" Motocicletta di tipo {self.get_tipo()}"




# inserire get_name in tutti
class GestoreParcoVeicoli:

    def __init__(self, veicoli=[]):
        self.__veicoli=[]

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


    def elimina_veicolo(self):
        print("Inserimento nuovo veicolo: ")
        modello = input("Digita il modello del veicolo da eliminare: ")
        #cerca il veicolo corrispondente
        for veicolo in self.__veicoli:
            if modello == veicolo.get_modello():
                veicolo_da_eliminare = veicolo
                break
        
            self.rimuovi(veicolo)
            self.aggiungi_veicolo(veicolo)
            print("Veicolo aggiunto al parco auto. ")


    def aggiungi_veicolo(self, veicolo):
        self.__veicoli.append(veicolo)

    def rimuovi_veicolo(self, veicolo):
        self.__veicoli.remove(veicolo)

    def stampa_lista_veicoli(self):
        print()
        print("Lista Veicoli")
        print()
        for veicolo in self.__veicoli:
            print(veicolo.info_base())


    def start(self):
        
        attivo = True
        while attivo == True:
            print()
            print("----------------------")
            print("Sistema Gestore Veicoli")
            print("----------------------")
            print("Digita: ")
            print("i per inserire veicolo")
            print("r per rimuovere veicolo")
            print("s per stampare lista veicoli")
            print("q per uscire")
            risposta = input(": ")
            
            if risposta == "i":
                self.crea_veicolo()
            elif risposta == "r":
                self.elimina_veicolo()
            elif risposta == 's':
                self.stampa_lista_veicoli()
            elif risposta == "q":
                attivo = False



mio_garage = GestoreParcoVeicoli()

mio_garage.start()