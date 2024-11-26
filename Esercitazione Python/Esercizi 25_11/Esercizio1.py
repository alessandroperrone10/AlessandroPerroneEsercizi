# Importare le librerie necessarie
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

#Applico l'algoritmo K-Nearest Neighbors
modello = KNeighborsClassifier(n_neighbors=5)
modello.fit(X_train, y_train)

#Valuto l'accuratezza del modello
previsioni = modello.predict(X_test)
accuratezza = accuracy_score(y_test, previsioni)


print(f'La precisione del modello è: {accuratezza:.2f}')


print(iris.feature_names)
print(X[1])
print(iris.target_names)
print(y[1])