
#Pca Standard
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
import pandas as pd

# Caricamento dati
data = load_iris()
X = pd.DataFrame(data.data, columns=data.feature_names)

# PCA con 2 componenti
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

print("Varianza spiegata:", pca.explained_variance_ratio_)




#Incremental PCA
from sklearn.decomposition import IncrementalPCA

# IPCA con 2 componenti
ipca = IncrementalPCA(n_components=2, batch_size=10)
X_ipca = ipca.fit_transform(X)

print("Varianza spiegata (IPCA):",
ipca.explained_variance_ratio_)





#Kernel PCA
from sklearn.decomposition import KernelPCA

# KPCA con kernel RBF
kpca = KernelPCA(n_components=2, kernel='rbf', gamma=15)
X_kpca = kpca.fit_transform(X)

print("Forma dati trasformati:", X_kpca.shape)




#Truncated SVD
from sklearn.decomposition import TruncatedSVD

# SVD troncata con 2 componenti
svd = TruncatedSVD(n_components=2, random_state=42)
X_svd = svd.fit_transform(X)

print("Varianza spiegata:", svd.explained_variance_ratio_)