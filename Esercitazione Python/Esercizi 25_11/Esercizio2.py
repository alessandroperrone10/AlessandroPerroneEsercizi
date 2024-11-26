# Importare le librerie necessarie
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


# Caricare il dataset Iris
iris = load_iris()
X = iris.data 
y = iris.target


#Suddivisione del dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modello = LinearRegression()
modello.fit(X_train, y_train)

#Valuto l'accuratezza del modello
previsioni = np.round(modello.predict(X_test)).astype(int)
accuratezza = accuracy_score(y_test, previsioni)


print(f'La precisione del modello è: {accuratezza:.2f}')

