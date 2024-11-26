from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

data = load_iris()
X = data.data  # le caratteristiche
y = data.target  # le etichette


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


print(X_scaled)
