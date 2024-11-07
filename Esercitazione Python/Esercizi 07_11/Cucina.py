
# Crea una classe ristorante con una lista di liste chiamata menu e una lista chiamata ordinazione, 
# Nel menu ci devono essere X piatti composti ogniuno da una lista propria di ingredienti, e
# la lista ordinazione invece e composta dalle singole ordinazioni del cliente 
# Servirrà quindi una classe cliente e ogni membro della cucina potrà servire solo X piatti

from abc import ABC,abstractmethod


class PersonaleCucina(ABC):
    def __init__(self,nome,età):
        self.__nome = nome
        self.__età = età
        self.ingredienti = []

    @abstractmethod
    def lavora():
        pass

    def get_nome(self):
        return self.__nome
    
    def set_nome(self,nome):
        self.__nome = nome

    def get_età(self):
        return self.__età
    
    def set_età(self,età):
        self.__età = età

class Chef(PersonaleCucina):
    def __init__(self, nome, età,specialità):
        super().__init__(nome, età)
        self.__specialità = specialità

    def lavora(self):
        print(f"Lo chef {self.get_nome()}, sta supervisionando la cucina, pensando a nuove ricette")

    def get_specialità(self):
        return self.__specialità
    
    def set_specialità(self,specialità):
        self.__specialità = specialità

    def prepara_menu(self):
        print(f"Lo chef {self.get_nome()}, specializzato in {self.get_specialità()}, sta cucinando nuove ricette per il suo team")


class SousChef(PersonaleCucina):
    def __init__(self, nome, età,esperienza,specialità):
        super().__init__(nome, età)
        self.__esperienza = esperienza 
        self.__specialità = specialità

    def lavora(self):
        print(f"Il sous chef {self.get_nome()}, sta gestendo l'inventario e aiuta lo chef")

    def get_esperienza(self):
        return self.__esperienza

    def set_esperienza(self,esperienza):
        self.__esperienza = esperienza

    def gestisci_inventario():
        pass
    
    def get_specialità(self):
        return self.__specialità
    
    def set_specialità(self,specialità):
        self.__specialità = specialità
class CuocoLinea(PersonaleCucina):
    def __init__(self, nome, età, postazione,specialità):
        super().__init__(nome, età)
        self.__postazione = postazione
        self.__specialità = specialità

    def lavora(self):
        print(f"Il cuoco {self.get_nome()}, adetto ai {self.__postazione}, sta cucinando")

    def get_postazione(self):
        return self.__postazione
    
    def set_postazione(self,postazione):
        self.__postazione = postazione

    def cucina_piatto(nome_piatto):
        pass


class Ristorante:
    def __init__(self):
        self.menu = {}
        self.ordinazioni = []
        self.personale = []

    def aggiungi_piatto_al_menu(self,nome_piatto,ingredienti):
        self.menu[nome_piatto] = ingredienti

    def mosta_menu(self):
        print("Menu del ristorante")
        for piatto,ingredienti in self.menu.items():
            print(f"{piatto}: {ingredienti}")

    def aggiungi_personale(self,persona):
        self.personale.append(persona)
        
    
    def aggiungi_ordinazioni(self,nome_piatto):
        if nome_piatto in self.menu:
            self.ordinazioni.append(nome_piatto)
            print(self.ordinazioni)
        else:
            print("Il piatto che hai selezionato non c'è nel menù")


            

     


class Cliente:
    def __init__(self,nome):
        self.nome = nome
        self.ordinazioni = []

    def effettua_ordinazioni(self,ristorante,nome_piatto):
        self.ordinazioni.append(nome_piatto)
        ristorante.aggiungi_ordinazioni(nome_piatto)




ristorante = Ristorante()
cliente = Cliente("Franco")


chef = Chef("Alessandro",45,"Pasta al sugo")
souschef = SousChef("Giuseppe",32,4,"Pasta alla carbonara")
cuocodiLinea = CuocoLinea("Gianfranco",23,"fritti","Frittura di pesce")


ristorante.aggiungi_personale(chef)
ristorante.aggiungi_personale(souschef)
ristorante.aggiungi_personale(cuocodiLinea)


ristorante.aggiungi_piatto_al_menu("Pasta alla carbonara", ["pasta","guanciale","uova"])



ristorante.mosta_menu()
cliente.effettua_ordinazioni(ristorante,"Pasta alla carbonara")