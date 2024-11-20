# Utilizzare un dataset di esempio che include le seguenti informazioni su
# un gruppo di persone: Nome, Età, Città e Salario. 

# Caricare i dati in un DataFrame autogenerandoli casualmente .
# Visualizzare le prime e le ultime cinque righe del DataFrame.
# Visualizzare il tipo di dati di ciascuna colonna.
# Calcolare statistiche descrittive di base per le colonne numeriche (media,
# mediana, deviazione standard).
# Identificare e rimuovere eventuali duplicati.
# Gestire i valori mancanti sostituendoli con la mediana della rispettiva
# colonna.
# Aggiungere una nuova colonna chiamata "Categoria Età" che classifica le
# persone come "Giovane", "Adulto" o "Senior" basandosi sull'età (es., 0-18
# anni: Giovane, 19-65 anni: Adulto, oltre 65 anni: Senior).
# Salvare il DataFrame pulito in un nuovo file CSV.


import pandas as pd
import numpy as np


Nomi = ["Alessandro", "Marco", "Mario", "Luigi", "Toad","Wario","Yoshi","Waluigi"]

Età = np.random.randint(15, 30, size=8)

Città = ["Roma", "Milano", "Napoli", "Torino", "Tokyo", "Osaka", "New York", "Londra" ]

Salario = np.random.randint(1000, 5000, size=8)

dataframe = pd.DataFrame(data = {"Nome": Nomi, "Età": Età, "Città": Città, "Salario": Salario})

#Visualizzo il dataframe iniziale
print("DataFrame di partenza:")
print(dataframe)

#Visualizzo le prime e le ultime cinque righe del DataFrame
print(dataframe.head())
print(dataframe.tail())

#Visualizzo il tipo di dati di ciascuna colonna
print(dataframe.dtypes)

#Descrizione del dataframe
print(dataframe.describe())

#Cerco valori duplicati e li rimuovo
#print(dataframe.duplicated())
#dataframe = dataframe.drop_duplicates()

#Gestione dei valori mancanti sostituendoli con la mediana della rispettiva colonna
#dataframe["Età"].fillna(dataframe["Età"].median(), inplace=True)

#Aggiunta nuova colonna
dataframe2 = pd.DataFrame(dataframe, columns=("Nome", "Età", "Città", "Salario", "Categoria Età"))

def tipo_età(eta):
    if eta <= 18:
        return "Giovane"
    elif eta <= 65:
        return "Adulto"
    else:
        return "Senior"

dataframe2["Categoria Età"] = dataframe2["Età"].apply(tipo_età)

print("DataFrame modificato:")
print(dataframe2)



#Salvataggio del dataframe pulito in un nuovo file CSV
dataframe2.to_csv("dataframe_pulito.csv", index=False)
