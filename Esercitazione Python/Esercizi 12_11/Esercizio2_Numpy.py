# Create 2 array bidimensionali numpy 4x4 con valori interi casuali ed eseguite le seguenti operazioni:

# - Restituite la somma di tutti gli elementi dei singoli array che si trovano nell'ultima riga dalla seconda colonna in poi;
# - Unite i 2 array secondo l'asse 1.



import numpy as np


array1 = np.random.randint(0, 10, (4, 4))

array2 = np.random.randint(0, 10, (4, 4))

somma_array1 = np.sum(array1[-1, 1:])
print(f"La somma dell'array {array1} , è: {somma_array1}")
somma_array2 = np.sum(array2[-1, 1:])
print(f"La somma dell'array {array2} , è: {somma_array2}")


array_unito = np.concatenate((array1, array2), axis=1)
print("Array unito: ", array_unito)