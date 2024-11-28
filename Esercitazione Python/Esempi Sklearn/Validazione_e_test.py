#Train test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=42)


#K-fold Cross-validation
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
print('Accuratezza media:',scores.mean())


#Stratified K-Fold Cross-validation
from sklearn.model_selection import StratifiedKFold
skf = StratifiedKFold(n_splits=5)
for train_index, test_index in skf.split(X, y):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]




#Ezempio stratifiedFold
from sklearn.model_selection import StratifiedKFold

# Definizione di StratifiedKFold
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# Configurazione di RandomizedSearchCV con cv specificato
random_search_cv = RandomizedSearchCV(
    estimator=RandomForestClassifier(random_state=42),
    param_distributions=param_dist,
    n_iter=10,
    scoring='accuracy',
    cv=cv,
    random_state=42,
    n_jobs=-1
)

# Esecuzione della ricerca
random_search_cv.fit(X, y)

# Migliori parametri trovati
print("Migliori parametri (con StratifiedKFold):")
print(random_search_cv.best_params_)