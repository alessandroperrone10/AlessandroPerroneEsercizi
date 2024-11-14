# Create 1 array unidimensionale con 50 valori randomici compresi tra 1 e 1.000 e fate i seguenti calcoli:

# - Calcolo della media;
# - Calcolo della moda;
# - Calcolo della deviazione standard;
# - Trasformatelo in un array 5 X 10

import numpy as np
from scipy import stats


#Inizializzo array
array = np.random.randint(1, 1000, 50)
print("Array iniziale: ", array)

#Calcolo media
media = np.mean(array)
print("La media dell' array è :", media)

#Calcolo moda
moda = stats.mode(array)
deviazione_standard = np.std(array)

#Array 5 x 10
nuovo_array = array.reshape(5, 10)
print(nuovo_array)



select country.Name as nome_paese,countrylanguage.Language as lingua,city.Name as nome_citta
from country
INNER JOIN countrylanguage on country.Code = countrylanguage.CountryCode
INNER JOIN city ON country.Code = city.CountryCode;