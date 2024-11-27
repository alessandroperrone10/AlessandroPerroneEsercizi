import numpy as np
import pandas as pd
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split, RandomizedSearchCV, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from scipy.stats import randint as sp_randint
from scipy.stats import uniform

# Inizializzazione del dataset Wine
wine_data = load_wine()
X = wine_data.data  # Caratteristiche
y = wine_data.target  # Etichette

# Suddivisione in train e test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# Definizione della pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),          # Step 1: Standardizzazione
    ('pca', PCA()),                        # Step 2: PCA
    ('modello', GradientBoostingClassifier())  # Step 3: Classificazione
])

# Definizione della distribuzione degli iperparametri
param_dist = {
    'pca__n_components': sp_randint(5, 13),
    'modello__n_estimators': sp_randint(50, 200),
    'modello__learning_rate': uniform(0.01, 0.2),
    'modello__max_depth': sp_randint(1, 5),
    'modello__subsample': uniform(0.6, 0.4),
    'modello__min_samples_split': sp_randint(2, 10),
    'modello__min_samples_leaf': sp_randint(1, 10),
    'modello__max_features': ['auto', 'sqrt', 'log2', None]
}

# StratifiedKFold per mantenere le proporzioni delle classi
cross_validation = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# RandomizedSearchCV per ottimizzazione degli iperparametri
random_search = RandomizedSearchCV(
    pipeline, 
    param_distributions=param_dist, 
    n_iter=50, 
    cv=cross_validation,
    scoring='accuracy', 
    random_state=42, 
    n_jobs=-1
)

# Adatta il modello ai dati di training
random_search.fit(X_train, y_train)

# Miglior modello e punteggio
miglior_modello = random_search.best_estimator_
miglior_punteggio = random_search.best_score_

# Valutazione sul set di test
y_pred = miglior_modello.predict(X_test)

print("Prestazione del miglior modello: ")
print(miglior_modello)
print("\nIl miglior punteggio CV:", miglior_punteggio)
print("\nClassification Report (Test Set):")
print(classification_report(y_test, y_pred))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))