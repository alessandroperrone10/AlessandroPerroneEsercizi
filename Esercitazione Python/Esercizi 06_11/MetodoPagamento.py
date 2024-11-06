class MetodoPagamento:
    def __init__(self,tipo_pagamento):
        self.tipo_pagamento = tipo_pagamento

    def effettua_pagamento(self,importo):
        print(f"Pagamento di {importo} effettuato con {self.tipo_pagamento}")

class CartaDiCredito(MetodoPagamento):
    def __init__(self, tipo_pagamento, __numero_carta,titolare, data_scadenza, cvv):
        super().__init__(tipo_pagamento)
        self.__numero_carta = __numero_carta
        self.titolare = titolare
        self.data_scadenza = data_scadenza
        self.__cvv = cvv

    def get_numero_carta(self):
        return self.__numero_carta
    
    def set_numero_carta(self,numero_carta):
        self.__numero_carta = numero_carta

    def get_cvv(self):
        return self.__cvv
    
    def set_cvv(self,cvv):
        self.__cvv = cvv

    # def __test(self,titolare):
    #     if self.titolare == titolare:
    #         print("Accesso ")
        

    def effettua_pagamento(self, importo):
        print(f"Pagamento di {importo} effettuato da {self.titolare}")

class Paypal(MetodoPagamento):
    def __init__(self, tipo_pagamento,__email):
        super().__init__(tipo_pagamento,)
        self.__email = __email

    def get_email(self):
        return self.__email
    
    def set_email(self,email):
        self.__email = email

    def effettua_pagamento(self, importo):
        print(f"Pagamento di {importo}, ricevuta disponiile sulla seguente mail: {self.__email}")

class BonificoBancario(MetodoPagamento):
    def __init__(self, tipo_pagamento,__iban,titolare):
        super().__init__(tipo_pagamento)
        self.__iban = __iban
        self.titolare = titolare

    def get_iban(self):
        return self.__iban
    
    def set_iban(self,iban):
        self.__iban = iban


    def effettua_pagamento(self, importo):
        input(f"Pagamento di {importo}, effettuato da {self.titolare}")


class GestorePagamenti:
    def __init__(self,metodo_pagamento):
        self.metodo_pagamento = metodo_pagamento


    def paga(self, importo):
        self.metodo_pagamento.effettua_pagamento(importo)



carta = CartaDiCredito("Carta di Credito",12345455,"Alessandro Perrone","20/04/2024","443")

paypal = Paypal("PayPal","alessandro@perrone.com")

bonifico = BonificoBancario("Bonifico",23112132323,"Perrone Alessandro")

gestore_carta = GestorePagamenti(carta)

importo = 100000

gestore_carta.paga(importo)