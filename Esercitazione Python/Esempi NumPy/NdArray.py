import numpy as np
from scipy import stats

# #Creazione array unidimensionale
arr = np.array([1,2,3,4,5])
print(stats.mode(arr))


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

# #Cambia la forma dell'array senza modificarne i dati
# arr = np.arange(6)
# print(arr)
# reshaped_arr = arr.reshape((6,1))
# print(reshaped_arr)





arr = np.array([1,2,3,4,5])
# #Indexing
# print(arr[0])
# #Slicing
#print(arr[1:3])
# #Boolean Indexing
# print(arr[arr > 2])

# print(arr[1:8:2])

print(arr[::3])
#print(arr[5:])

#print(arr[-1:])



#arr_2d = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

#Slicing sulle righe
#print(arr_2d[1:3])

#Slicing sulle colonne
#print(arr_2d[:,1:3])

#Slicing misto
#print(arr_2d[1:, 1:3])





# arr = np.array([10,20,30,40,50])

# indice = np.array([0,3,4])

# indice = [0,3,4]

# print(arr[indice])