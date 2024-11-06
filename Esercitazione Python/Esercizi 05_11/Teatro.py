class Posto:
    def __init__(self,numero,fila):
        self.__numero = numero
        self.__fila = fila
        self.__occupato = False
        self.tipo_posto = ""


    def get_numero(self):
        return self.__numero

    def set_numero(self,numero):
        self.__numero = numero

    def get_fila(self):
        return self.__fila

    def set_fila(self,fila):
        self.__fila = fila

    def get_occupato(self):
        return self.__occupato

    def set_occupato(self,occupato):
        self.__occupato = occupato

    def prenota(self):
        if self.__occupato == False:
            self.__occupato = True
            print(f"Hai prenotato il tuo posto in sala! Il posto è: Fila:{self.__fila}, Posto:{self.__numero} ")
        else:
            print(f"Il posto Fila:{self.__fila},Posto:{self.__numero}, è già occupato")

    def libera(self):
        if self.__occupato == True:
            self.__occupato = False
            print(f"Il posto Fila:{self.__fila},Posto:{self.__numero}, ora è libero")
        else:
            print(f"Il posto Fila:{self.__fila},Posto:{self.__numero}, è già libero")

class PostoVIP(Posto):
    def __init__(self, __numero, __fila):
        super().__init__(__numero, __fila)
        self.tipo_posto = "Vip"
        self.servizi_extra = "Servizio al posto"

    def prenota(self):
        occupato = self.get_occupato()
        if occupato == False:
            self.set_occupato(True)
            print(f"Hai prenotato il tuo posto VIP in sala! Il posto è: Fila:{self.get_fila()}, Posto:{self.get_numero()}, con Servizio Extra: {self.servizi_extra}")
        else:
            print(f"Il Posto che hai scelto è già prenotato")

class PostoStandard(Posto):
    def __init__(self,__numero,__fila):
        super().__init__(__numero,__fila)
        self.tipo_posto = "Standard"
        self.costo_extra = 5.00

    def prenota(self):
        occupato = self.get_occupato()
        if occupato == False:
            self.set_occupato(True)
            print(f"Hai prenotato il tuo posto Standard in sala! Il posto è: Fila:{self.get_fila()}, Posto:{self.get_numero()}, con un costo extra di: {self.costo_extra}")
        else:
            print(f"Il Posto che hai selezionato è già prenotato")


class Teatro:
    def __init__(self):
        self.__posti = {}

    def aggiungi_posto(self,posto):
        tipo = posto.tipo_posto
        if tipo not in self.__posti:
            self.__posti[tipo] = []
        self.__posti[tipo].append(posto)

    def stampa_posti_occupati():
        pass

    def prenota_posto(self,numero,fila,tipo_posto):
        if tipo_posto in self.__posti:
            for posto in self.__posti[tipo_posto]:
                if posto.get_numero() == numero and posto.get_fila() == fila:
                    posto.prenota()
                    
        else:
            print("Tipo di posto non valido")


teatro = Teatro()

posto = Posto(10,"A")
postoVIP = PostoVIP(15,"B")
postoVIP2 = PostoVIP(17,"B")
postoStandard = PostoStandard(11,"C")

teatro.aggiungi_posto(postoVIP)
teatro.aggiungi_posto(postoVIP2)
teatro.aggiungi_posto(postoStandard)

teatro.prenota_posto(11,"C","Standard")

teatro.prenota_posto(13,"C","Standard")

#posto.prenota()


