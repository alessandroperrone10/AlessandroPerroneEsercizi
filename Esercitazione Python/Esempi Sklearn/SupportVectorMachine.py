from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits
from sklearn.metrics import classification_report

# Caricamento del dataset
data = load_digits()
X = data.data
y = data.target

# Suddivisione in training e test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Creazione del modello
model = SVC(kernel='rbf', C=1.0, gamma='scale', random_state=42)

# Addestramento del modello
model.fit(X_train, y_train)

# Predizione
y_pred = model.predict(X_test)

# Valutazione
print(classification_report(y_test, y_pred))