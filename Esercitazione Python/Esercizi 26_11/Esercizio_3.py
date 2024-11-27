from sklearn.datasets import load_wine
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV


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


#creo il modello con RandomForestClassifier
modello = RandomForestClassifier(random_state=42)

#Addestramento del modello
modello.fit(X_train, y_train)

#Valuto l'accuratezza del modello
previsioni = modello.predict(X_test)

classificazione = classification_report(y_test, previsioni, target_names=wine_data.target_names)
print("Classificazione del modello:\n", classificazione)

#Visualizza le feature più importanti del dataset Wine secondo il modello Random Forest, utilizzando un grafico a barre.
importances = modello.feature_importances_
indices = np.argsort(importances)[::-1]

plt.figure(figsize=(10, 6))
plt.bar(range(X.shape[1]), importances[indices])



# Genera la matrice di confusione
matrice = confusion_matrix(y_test, previsioni)

# Visualizza la matrice di confusione con una heatmap
plt.figure(figsize=(8,6))
sns.heatmap(matrice, annot=True, fmt='d', xticklabels=wine_data.target_names, yticklabels=wine_data.target_names)
plt.title('Matrice di Confusione')
plt.xlabel('Predetto')
plt.ylabel('Reale')
plt.show()


#Utilizza la GridSearchCV per ottimizzare i parametri del Random Forest (ad esempio: numero di estimatori e profondità massima dell'albero).

param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 5, 10, 15]
}

grid_search = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=5)
grid_search.fit(X_train, y_train)

#Visualizza i risultati ottenuti dalla GridSearchCV
print("Risultati della GridSearchCV:\n", grid_search.best_params_)
