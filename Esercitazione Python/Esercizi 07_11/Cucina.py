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
    def __init__(self, nome, età,ingredienti,specialità):
        super().__init__(nome, età, ingredienti)
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
    def __init__(self, nome, età,ingredienti,esperienza):
        super().__init__(nome, età, ingredienti)
        self.__esperienza = esperienza 

    def lavora(self):
        print(f"Il sous chef {self.get_nome()}, sta gestendo l'inventario e aiuta lo chef")

    def get_esperienza(self):
        return self.__esperienza

    def set_esperienza(self,esperienza):
        self.__esperienza = esperienza

    def gestisci_inventario():
        pass

class CuocoLinea(PersonaleCucina):
    def __init__(self, nome, età, ingredienti,postazione):
        super().__init__(nome, età, ingredienti)
        self.__postazione = postazione

    def lavora(self):
        print(f"Il cuoco {self.get_nome()}, adetto ai {self.__postazione}, sta cucinando")

    def get_postazione(self):
        return self.__postazione
    
    def set_postazione(self,postazione):
        self.__postazione = postazione

    def cucina_piatto(nome_piatto):
        pass