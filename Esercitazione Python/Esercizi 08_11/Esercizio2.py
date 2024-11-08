import numpy as np


class Array:
    def __init__(self):
        self.array = np.random.randint(10, 51, 20)


    def stampa_array(self):
        print(self.array)

    def forma_array(self):
        print(self.array.shape) 

    def primi_dieci_numeri(self):
        print(self.array[:10])

    def ultimi_cinque_numeri(self):
        print(self.array[-5:])

    def da_cinque_a_quindici(self):
        print(self.array[5:15])

    def ogni_terzo_elemento(self):
        lista = self.array.reshape(4,5)
        print("Array splittato: ",lista)
        print(lista[:,2])

    def valore_99(self):
        self.array[5:10] = 99
        print(self.array)
        

array = Array()


array.stampa_array()

#array.forma_array()

array.primi_dieci_numeri()

array.ultimi_cinque_numeri()

array.da_cinque_a_quindici()

array.ogni_terzo_elemento()

#array.valore_99()