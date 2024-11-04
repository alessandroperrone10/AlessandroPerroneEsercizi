class Ristorante:

    def __init__(self,nome,tipo_cucina):
    
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        #self.aperto = False
        #self.menu = {}


    def inserimento_ristorante(self):
        ristoranti = {}

        ristoranti = {
            self.nome : {
                "tipo_cucina" : self.tipo_cucina,
                "aperto" : False,
                "menu" : {}
            }
        }

        print(ristoranti.items())



class GestioneRistorante:

    def __init__(self):
        pass

    def descrivi_ristorante():
        pass

    def stato_aperture():
        pass

    def apri_ristorante():
        pass

    def chiudi_ristorante():
        pass

    def aggiungi_al_menu():
        pass

    def togli_dal_menu():
        pass

    def stampa_menu():
        pass
    



    
nome = input("Inserisci il nome del ristorante: ")
tipo_cucina = input("Inserisci il tipo di cucina del ristorante: ")

ristorante = Ristorante(nome,tipo_cucina)


ristorante.inserimento_ristorante()





    