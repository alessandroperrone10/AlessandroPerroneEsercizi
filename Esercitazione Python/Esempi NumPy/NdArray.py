import numpy as np

# #Creazione array unidimensionale
# arr = np.array([1,2,3,4,5])


# #Creazione array bidimensionale
# arr2d = np.array([[1,2,3],[4,5,6]])


# #Metodi di ndarray
# #Dimensione dell'array
# print("Forma dell'array: ",arr2d.shape)


# #Tipo di dati
# print("Dimensioni dell'array: ", arr.dtype)


## Creazione array con una sequenza di numeri
# arr = np.arange(10)
# print(arr)

#Cambia la forma dell'array senza modificarne i dati
arr = np.arange(6)
print(arr)
reshaped_arr = arr.reshape((6,1))
print(reshaped_arr)