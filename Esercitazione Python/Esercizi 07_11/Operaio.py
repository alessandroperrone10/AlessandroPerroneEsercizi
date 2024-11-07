from abc import ABC,abstractmethod


class Operaio:
    def __init__(self,nome,età):
        self.nome = nome
        self.età = età
        self.status = False

    def lavora(self):
        if self.status == False:
            self.status = True
            print("Inizio a lavorare")
        else:
            print("Sto già lavorando")


class Martello(ABC):
    
    @abstractmethod
    def usa():
        pass


class Trapano(ABC):

    @abstractmethod
    def usa():
        pass


class Muratore(Operaio,Martello):
    def __init__(self, nome, età):
        super().__init__(nome, età)

    def usa():
        print("Sto usando il martello! Occhio!")


class Carpentiere(Operaio,Trapano):
    def __init__(self, nome, età):
        super().__init__(nome, età)

    def usa():
        print("Sto usando il trapano!State attenti!")



muratore = Muratore("Alessandro",24)

muratore.lavora()

muratore.usa()


carpentiere = Carpentiere("Giuseppe",36)

muratore.lavora()

muratore.usa()