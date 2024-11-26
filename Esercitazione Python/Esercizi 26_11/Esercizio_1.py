from sklearn.datasets import load_iris
from sklearn.discriminant_analysis import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix


# Caricamento del dataset
data = load_iris()
X = data.data  # le caratteristiche
y = data.target  # le etichette


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)



# Divisione dei dati in set di addestramento e di test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# Creazione del modello di classificazione
modello = DecisionTreeClassifier()


# Addestramento del modello
modello.fit(X_train, y_train)


# Predizione delle etichette per il set di test
predictions = modello.predict(X_test)

#Valuta la performance del modello utilizzando il classification_report (precisione, recall, F1-score)
classificazione = classification_report(y_test, predictions, target_names=data.target_names)
print("Classificazione del modello: \n", classificazione)


#Visualizzazione della matrice di confusione
matrice_confusione = confusion_matrix(y_test, predictions)

print("Matrice di confusione: \n", matrice_confusione)

