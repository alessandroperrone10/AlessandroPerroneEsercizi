class ContoBancario:
    def __init__(self,):
        self.__titolare = ""
        self.__saldo = 0

    def get_titolare(self):
            return self.__titolare

    def set_titolare(self,titolare):
        self.__titolare = titolare

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self,saldo):
        self.__saldo = saldo


    def deposita(self,importo):
        self.__saldo += importo

    def preleva(self,importo):
        self.__saldo -= importo

    def visualizza_saldo(self):
        return self.get_saldo()


conto = ContoBancario()

conto.set_titolare("Alessandro")

print("Ciao: ",conto.get_titolare())
print("Il tuo saldo è di: ",conto.visualizza_saldo())

#Funzione deposita
conto.deposita(100)
print("Deposito effettuato")
print("Il tuo saldo è :",conto.visualizza_saldo())

#Funzione preleva
conto.preleva(100)
print("Prelevo effettuato")
print("Il tuo saldo ora è di: ",conto.visualizza_saldo())


