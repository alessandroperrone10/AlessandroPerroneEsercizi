from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston
from sklearn.metrics import mean_squared_error

# Caricamento del dataset
X, y = load_boston(return_X_y=True)

# Suddivisione dei dati in training e test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creazione del modello di regressione lineare
model = LinearRegression(fit_intercept=True, normalize=False, copy_X=True, n_jobs=None)

# Addestramento del modello
model.fit(X_train, y_train)

# Predizione sui dati di test
y_pred = model.predict(X_test)

# Calcolo dell'errore quadratico medio
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Stampa dei coefficienti
print("Coefficienti:", model.coef_)
print("Intercetta:", model.intercept_)