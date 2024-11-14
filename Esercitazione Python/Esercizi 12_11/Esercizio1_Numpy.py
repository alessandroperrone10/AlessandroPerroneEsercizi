# Crea 2 array numpy:
# Un array unidimensionale di numeri casuali compresi tra 0 e 1;
# Un array bidimensionale di dimensione 3x3 con valori interi casuali.


import numpy as np

primo_array = np.random.rand(5)

secondo_array = np.random.randint(0, 20, (3, 3))

print("Array unidimensionale: ", primo_array)

print("Array bidimensionale: ", secondo_array)

