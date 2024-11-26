
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

#Inizializzazione del dataset Wine
wine_data = load_wine()
X = wine_data.data  # Caratteristiche
y = wine_data.target  # Etichette


#Standardizzazione delle caratteristiche utilizzando la classe StandardScaler per portare tutte le feature su una scala comune
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


#Suddivisione dei dataset in training set e test set. 70% per il training, il 30% per il test
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

#Creazione modello con DecisionTreeClassifier
model = DecisionTreeClassifier()


#addestramento del modello
model.fit(X_train, y_train)

#Valutazione performance del modello con classification_report
y_pred = model.predict(X_test)
classificazione_report = classification_report(y_test, y_pred, target_names= wine_data.target_names)
print("Classificazione del modello:\n", classificazione_report)


#visualizzazione della matrice di confusione
matrice_confusione = confusion_matrix(y_test, y_pred)
print("Matrice di confusione:\n", matrice_confusione)