import pandas as pd
import numpy as np

#10 righe, 3 colonne e riempitelo di numeri random

# frame = pd.DataFrame({
#     "prima_colonna": np.random.randint(1, 10, size= 10),
#     "seconda_colonna": np.random.randint(10, 20, size=10),
#     "terza_colonna": np.random.randint(20, 30, size=10)
# })

# print(frame)


#creare una serie di 15 numeri random, inserire un valore nullo a 3 indici generati randomicamente, riempirli poi con ffill

serie = pd.Series(np.random.randint(1, 100, size=15))

serie[np.random.choice(range(15), 3, replace= False)] = np.nan

print(serie)

serie = serie.ffill()

print(serie)