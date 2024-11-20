import numpy as np
import pandas as pd

#Percorso del file CSV
file_path = 'Esercitazione Python/Esercizi 19_11/train.csv'

# Caricamneto dei dati nel DataFrame
df = pd.read_csv(file_path)

#le prime righe del DataFrame per confermare
print(df.head())

print(df.info())

print(df.describe())




#passenger id è la chiave univoca del file
#la variabile survived è un booleano 0 = no, 1 = yes
#età può essere vuoto il campo
#cabina può essere vuoto il campo
#embarked può essere vuoto il campo C = Cherbourg, Q = Queenstown, S = Southampton

#tipi di variabili
#int : PassengerId, Pclass, SibSp, Parch, Survived
#float : Age, Fare
#object/stringhe : Name, Sex, Ticket, Cabin, Embark