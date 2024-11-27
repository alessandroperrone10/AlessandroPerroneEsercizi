from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# Generazione di dati sintetici
X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Creazione del modello
kmeans = KMeans(n_clusters=4, init='k-means++', n_init=10, max_iter=300, random_state=42)

# Addestramento del modello
kmeans.fit(X)

# Predizione dei cluster
y_kmeans = kmeans.predict(X)

# Visualizzazione dei cluster
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
centri = kmeans.cluster_centers_
plt.scatter(centri[:, 0], centri[:, 1], c='red', s=200, alpha=0.75)
plt.title('Clustering con K-Means')
plt.show()