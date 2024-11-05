class Animale:
    def __init__(self,nome,eta):
        self.nome = nome
        self.eta = eta

    def fai_suono(self):
        pass



class Canide(Animale):
    def __init__(self, nome, eta, tipo):
        super().__init__(nome, eta)
        self.tipo = tipo

    def aggiungi_canide(self):
        canide += 1
        


class Volatile(Animale):
    def __init__(self, nome, eta, tipo):
        super().__init__(nome, eta)
        self.tipo = tipo

    def aggiungi_volatile(self):
        volatile += 1
        




class Zoo:
    lista_animali = []

    def aggiungi_animali(self):
        if True:
            #animale = Animale()
            canide = Canide()