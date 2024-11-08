import numpy as np

class Lista:
    def __init__(self):
        self.lista = np.arange(10,50)


    def verifica_tipo(self):
        print(self.lista.dtype)

    def stampa_array(self):
        print(self.lista)

    def cambia_tipo(self):
        self.lista = np.arange(10.00,50.00)
        print(self.lista.dtype)

    def forma_array(self):
        print(self.lista.shape)



lista = Lista()

#Stampo
lista.stampa_array()

#Verifico il tipo
lista.verifica_tipo()

#Cambio il tipo
lista.cambia_tipo()

#Mostro forma dell'array
lista.forma_array()