from sklearn.datasets import load_wine
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


#Inizializzazione del dataset Wine
wine_data = load_wine()
X = wine_data.data  # Caratteristiche
y = wine_data.target  # Etichette




#Visualizza il numero di campioni per ciascuna classe e calcola le statistiche di base delle feature.
data_frame = pd.DataFrame(X, columns=wine_data.feature_names)

y_series = pd.Series(y)

#Visualizza il numero di campioni per ciascuna classe
class_counts = y_series.value_counts(sort=False)

print("Numero di campioni per ciascuna classe: \n",class_counts)
print("\nStatistiche di base delle feature:\n", data_frame.describe())

#creazione grafico a barre per mostrare la distribuzione delle classi
plt.figure(figsize=(10, 6))
plt.bar(wine_data.target_names, class_counts)
plt.xlabel("Classe")
plt.ylabel("Numero di campioni")
plt.title("Distribuzione delle classi")
plt.show()



#Divido il set in dati di training e di test. 80% training, 20% set

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


