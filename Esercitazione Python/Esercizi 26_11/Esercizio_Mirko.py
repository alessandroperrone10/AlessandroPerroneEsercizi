# Importa le librerie necessarie
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Moduli di scikit-learn
from sklearn.datasets import load_wine
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score, precision_score, recall_score, f1_score, confusion_matrix)

# Configura le visualizzazioni
#matplotlib inline
sns.set(style='whitegrid')

# Carica il dataset Wine
wine = load_wine()
X = wine.data
y = wine.target
feature_names = wine.feature_names
target_names = wine.target_names

# Crea un DataFrame per una migliore manipolazione
df = pd.DataFrame(X, columns=feature_names)
df['target'] = y

# Visualizza il numero di campioni per ciascuna classe
class_counts = df['target'].value_counts()
print("Numero di campioni per ciascuna classe:")
print(class_counts)

# Calcola le statistiche di base delle feature
feature_stats = df.describe()
print("\nStatistiche di base delle feature:")
print(feature_stats)

# Grafico a barre per mostrare la distribuzione delle classi
plt.figure(figsize=(8,6))
sns.countplot(x='target', data=df, palette='Set2')
plt.title('Distribuzione delle classi nel dataset Wine')
plt.xlabel('Classe')
plt.ylabel('Numero di campioni')
plt.xticks(ticks=[0,1,2], labels=target_names)
plt.show()

# Applica PCA per ridurre a 2 componenti principali
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Crea un DataFrame per le componenti principali
df_pca = pd.DataFrame(data=X_pca, columns=['PC1', 'PC2'])
df_pca['target'] = y

# Grafico scatter delle componenti principali
plt.figure(figsize=(10,8))
sns.scatterplot(data=df_pca, x='PC1', y='PC2', hue='target', palette='Set1', s=100)
plt.title('PCA del dataset Wine')
plt.xlabel('Prima Componente Principale')
plt.ylabel('Seconda Componente Principale')
plt.legend(title='Classe', labels=target_names)
plt.show()

# Dividi i dati in 80% training e 20% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inizializza il modello RandomForestClassifier
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

# Predici le classi sul test set
y_pred = clf.predict(X_test)

# Calcola le metriche di performance
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')  # 'weighted' per problemi multiclasse
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

print("\nPerformance del modello Random Forest:")
print(f"Accuratezza: {accuracy:.2f}")
print(f"Precisione: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1-score: {f1:.2f}")

# Ottieni l'importanza delle feature dal modello
importances = clf.feature_importances_
indices = np.argsort(importances)[::-1]  # Ordina in ordine decrescente

# Crea un grafico a barre delle feature più importanti
plt.figure(figsize=(12,6))
sns.barplot(x=[feature_names[i] for i in indices], y=importances[indices], palette='viridis')
plt.title('Importanza delle feature secondo Random Forest')
plt.xlabel('Feature')
plt.ylabel('Importanza')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Genera la matrice di confusione
cm = confusion_matrix(y_test, y_pred)

# Visualizza la matrice di confusione con una heatmap
plt.figure(figsize=(8,6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=target_names, yticklabels=target_names)
plt.title('Matrice di Confusione')
plt.xlabel('Predetto')
plt.ylabel('Reale')
plt.show()

# Definisci la griglia di parametri da cercare per l'ottimizzazione
param_grid = {
    'n_estimators': [50, 100, 150],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5],
    'min_samples_leaf': [1, 2]
}

# Inizializza GridSearchCV per ottimizzare il modello
grid_search = GridSearchCV(estimator=RandomForestClassifier(random_state=42),
                           param_grid=param_grid, cv=5, scoring='accuracy', n_jobs=-1)
grid_search.fit(X_train, y_train)

# Mostra i migliori parametri trovati
print("\nMigliori parametri trovati:")
print(grid_search.best_params_)

# Utilizza il miglior modello trovato
best_clf = grid_search.best_estimator_

# Predici sul test set con il modello ottimizzato
y_pred_optimized = best_clf.predict(X_test)

# Calcola le metriche di performance del modello ottimizzato
accuracy_opt = accuracy_score(y_test, y_pred_optimized)
precision_opt = precision_score(y_test, y_pred_optimized, average='weighted')
recall_opt = recall_score(y_test, y_pred_optimized, average='weighted')
f1_opt = f1_score(y_test, y_pred_optimized, average='weighted')

print("\nPerformance del modello Random Forest Ottimizzato:")
print(f"Accuratezza: {accuracy_opt:.2f}")
print(f"Precisione: {precision_opt:.2f}")
print(f"Recall: {recall_opt:.2f}")
print(f"F1-score: {f1_opt:.2f}")

# Genera la matrice di confusione per il modello ottimizzato
cm_opt = confusion_matrix(y_test, y_pred_optimized)

# Visualizza la matrice di confusione del modello ottimizzato
plt.figure(figsize=(8,6))
sns.heatmap(cm_opt, annot=True, fmt='d', cmap='Greens',
            xticklabels=target_names, yticklabels=target_names)
plt.title('Matrice di Confusione (Modello Ottimizzato)')
plt.xlabel('Predetto')
plt.ylabel('Reale')
plt.show()