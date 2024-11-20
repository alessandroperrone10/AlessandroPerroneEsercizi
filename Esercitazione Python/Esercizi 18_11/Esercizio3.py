# Utilizzare un dataset che registra le vendite di prodotti in diverse
# città, includendo le colonne Prodotto, Quantità, Prezzo Unitario e Città.



# Caricare i dati in un DataFrame.
# Aggiungere una colonna "Totale Vendite" che sia il risultato del prodotto tra
# Quantità e Prezzo Unitario.
# Raggruppare i dati per Prodotto e calcolare il totale delle vendite per
# ciascun prodotto.
# Trovare il prodotto più venduto in termini di Quantità.
# Identificare la città con il maggior volume di vendite totali.
# Creare un nuovo DataFrame che mostri solo le vendite superiori a un certo
# valore (es., 1000 euro).
# Ordinare il DataFrame originale per la colonna "Totale Vendite" in ordine
# decrescente.
# Visualizzare il numero di vendite per ogni città.

import pandas as pd
import numpy as np


# Generazione dei dati random

prodotti = ["Pizza", "Pasta", "Mandolino", "Marmo", "Iphone", "Box Pokemon", "Panda", "Panini", "Fraselli"]
città = ["Lecce", "Napoli", "Pordenone", "Pontedera", "Milano", "Brindisi", "Squinzano", "Campi", "Cerano"]

data = {
    "Prodotto": np.random.choice(prodotti, 8),
    "Città": np.random.choice(città, 8),
    "Prezzo Unitario": np.random.randint(10, 1000, 8),
    "Quantità": np.random.randint(1, 100, 8),
}

dataframe = pd.DataFrame(data)

print("Data frame inizale: ")
print(dataframe)

#Aggiunta colonna Totale Vendite
dataframe["Totale Vendite"] = dataframe["Quantità"] * dataframe["Prezzo Unitario"]
print("Nuovo data frame con totale vendite: ")
print(dataframe)

#Group by Prodotto e faccio la somma del totale vendite
grouped = dataframe.groupby("Prodotto")["Totale Vendite"].sum()
print(grouped)


#Prodotto più venduto
print("Prodotto più venduto: ", grouped.idxmax())


#Città con il maggior volume di vendite totali
print(dataframe.groupby("Città")["Totale Vendite"].sum().idxmax())


#Nuovo DataFrame con vendite superiori a 1000 euro
dataframe_superiori_1000 = dataframe[dataframe["Totale Vendite"] > 1000]
print("Data frame con vednite maggiori di 1000: ", dataframe_superiori_1000)


#Ordinamento per Totale Vendite in ordine decrescente
dataframe_ordinato = dataframe.sort_values(by="Totale Vendite", ascending=False)
print("Data frame ordinato per Totale Vendite: ")
print(dataframe_ordinato)


#Numero di vendite per ogni città
