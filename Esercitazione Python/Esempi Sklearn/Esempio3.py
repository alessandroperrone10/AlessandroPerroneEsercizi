from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error

data = load_iris()
X = data.data  # le caratteristiche
y = data.target  # le etichette


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


#Suddivisione del DataSet
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

#Regressione lineare
model = LinearRegression()
model.fit(X,y)
predictions = model.predict(X)

accuracy = accuracy_score(y_test, predictions)

#K - Nearest Neighbors
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)
predictions_knn = knn.predict(X)

mse = mean_squared_error(y_test, predictions_knn)