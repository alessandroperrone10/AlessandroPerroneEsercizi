# Utilizzare NumPy per generare una serie temporale
# di 305 giorni di dati, simulando il numero di visitatori giornalieri in
# un ospedale. Assumere che il numero medio di visitatori sia 1200 con una
# deviazione standard di 900. Inoltre, aggiungere un trend decrescente nel
# tempo per simulare l'aumento della popolarità del parco.


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#Dati iniziali
giorni = np.random.randint(1,306)
media_visitatori = 1200
deviazione_standard = 900

#Serie temporale dei visitatori
visitatori_giornalieri = np.random.normal(loc = media_visitatori, scale = deviazione_standard, size = giorni).astype(int)
visitatori_giornalieri = np.maximum(0, visitatori_giornalieri)


#Aggiunta trend decrescente
trend_decrescente = np.linspace(0, -300, giorni).astype(int)
visitatori_con_trend = visitatori_giornalieri + trend_decrescente
visitatori_con_trend = np.maximum(0, visitatori_con_trend)



# Creare un DataFrame pandas con le date come
# indice e il numero di visitatori come colonna e una collonna casuale
# della patologia scelta fra 3(ossa, cuore, testa ).


#colonna date 
date = pd.date_range(start="2023-01-01", periods=giorni, freq="D")

#colonna patologie
patologie = np.random.choice(["ossa", "cuore", "testa"], size=giorni)


#Creazione DataFrame

df = pd.DataFrame(index = date, data={'Visitatori': visitatori_con_trend, 'Patologia': patologie})

#Imposto il valore none alla colonna patologie per le righe con zero visitatori
df.loc[df['Visitatori'] == 0, 'Patologia'] = None


print(df)


print(df.describe())




# Creare un grafico a linee del numero di visitatori giornalieri.
# Aggiungere al grafico la media mobile a 7 giorni per mostrare la
# tendenza settimanale.
# Creare un secondo grafico che mostri la media mensile dei visitatori.
# creare un grafico che mostri la divisione fra le 3 patologie 


plt.figure(figsize=(15,10))
plt.plot(x = df.index, y = df["Visitatori"], label = 'Visitatori totali per giorno')
plt.xlabel('Data', fontsize=14)
plt.ylabel('Numero di visitatori', fontsize= 14)
plt.show()