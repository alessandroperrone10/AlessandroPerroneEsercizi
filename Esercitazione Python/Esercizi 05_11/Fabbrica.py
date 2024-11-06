class Prodotto:
    
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita

    def calcola_profitto(self):
        profitto = self.prezzo_vendita - self.costo_produzione
        if profitto < 0.00:
            print("Con la vendita di questo prodotto siamo in perdita di:", profitto, "€.")
        elif profitto == 0.00:
            print("Con la vendita di questo prodotto siamo in pari.")
        else:
            print("Con la vendita siamo in profitto di:", profitto, "€.")

    def visualizza_prodotto(self):
        print(f"Il prodotto è {self.nome}")


class Elettronica(Prodotto):

    def __init__(self, nome, costo_produzione, prezzo_vendita,__classe_energetica):
        super().__init__(nome, costo_produzione, prezzo_vendita)
        self.__classe_energetica = __classe_energetica

    def get_classe_energetica(self):
        return self.__classe_energetica

    def set_classe_energetica(self,classe):
        self.__classe_energetica = classe

    def visualizza_prodotto(self):
        print(f"Il prodotto è {self.nome} , con classe: {self.get_classe_energetica()}")
class Abbigliamento(Prodotto):

    def __init__(self, nome, costo_produzione, prezzo_vendita,__materiale):
        super().__init__(nome, costo_produzione, prezzo_vendita)
        self.__materiale = __materiale
      
    def get_materiale(self):
        return self.__materiale

    def set_materiale(self,materiale):
        self.__materiale = materiale

    def visualizza_prodotto(self):
        print(f"Il prodotto è {self.nome}, con classe: {self.get_materiale()}")


class Fabbrica:
    def __init__(self):
        self.inventario = {}

    def popolamento_inventario(self, nome):
        if nome not in self.inventario:
            self.inventario[nome] = 0
            print("Prodotto ",nome," aggiunto all'inventario con quantità iniziale 0.")
        else:
            print("Il prodotto ",nome," è già presente nell'inventario.")
        print("Inventario:", self.inventario)

    def aggiungi_prodotto(self, nome, quantita):
        if nome in self.inventario:
            self.inventario[nome] += quantita
            print("Aggiunti ",quantita, "pezzi di ",nome," all'inventario. Totale:" ,self.inventario[nome])
        else:
            print("Errore: il prodotto ",nome," non è presente nell'inventario. Usa 'popolamento_inventario' prima di aggiungere.")

    def vendi_prodotti(self, nome, quantita):
        if nome in self.inventario:
            if self.inventario[nome] >= quantita:
                self.inventario[nome] -= quantita
                print("Venduti ",quantita," pezzi di ",nome,".Rimanenti:" ,self.inventario[nome])
                prodotto1.calcola_profitto()
            else:
                print(f"Errore: non ci sono abbastanza pezzi di '{nome}' in inventario per la vendita.")
        else:
            print(f"Errore: il prodotto '{nome}' non è presente nell'inventario.")

    def resi_prodotti(self, nome, quantita):
        if nome in self.inventario:
            self.inventario[nome] += quantita
            print("Aggiunti ",quantita, "pezzi come reso per ",nome,". Totale: ",self.inventario[nome])
        else:
            print("Errore: il prodotto ",nome," non è presente nell'inventario.")

# Richiamo tutte le classi
fabbrica = Fabbrica()
# prodotto1 = Prodotto("lampada", 5.00, 10.00)

# # Calcola profitto
# prodotto1.calcola_profitto()

# # Aggiungi prodotto all'inventario
# fabbrica.popolamento_inventario(prodotto1.nome)

# # Aggiungi quantità di prodotto
# fabbrica.aggiungi_prodotto(prodotto1.nome, 1)

# # Vendi quantità di prodotto
# fabbrica.vendi_prodotti(prodotto1.nome, 1)

# # Rendi quantità di prodotto
# fabbrica.resi_prodotti(prodotto1.nome, 1)

def VisualizzaProdotto(placeholder):
    placeholder.visualizza_prodotto()


prodotto1 = Prodotto("lampada", 5.00, 10.00)

lavatrice = Elettronica("lavatrice", 50.00, 200.00, "A++")

maglietta = Abbigliamento("felpa", 20.00, 80.00, "cotone")



visualizza = VisualizzaProdotto(lavatrice)