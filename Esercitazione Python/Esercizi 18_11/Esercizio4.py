import pandas as pd
import numpy as np

data = {
'Student': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie'],
'Subject': ['Math', 'Math', 'Math', 'Science', 'Science', 'Science', 'English', 'English', 'English'],
'Score': [85, 90, 95, 80, 70, 75, 88, 92, 85]
}

df = pd.DataFrame(data)

print("DataFrame originale: ")
print(df)



#Inserisco altri voti agli studenti
data2 = {
'Student': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie'],
'Subject': ['Math', 'Math', 'Math', 'Science', 'Science', 'Science', 'English', 'English', 'English'],
'Score': [45, 55, 60, 70, 44, 100, 22, 33, 66]
}
df2 = pd.DataFrame(data2)

nuovo_df = pd.concat([df, df2])


print("\nDataFrame modificato: ")
print(nuovo_df)


#calcolare la media dei voti per ogni materia
media = nuovo_df.groupby('Subject')['Score'].mean()
print("Media dei voti per materia: ")
print(media)

#calcolare la media dei voti di ogni studente
media_studente = nuovo_df.groupby('Student')['Score'].mean()
print("Media dei voti per studente: ")
print(media_studente)


#calcolare la media di ogni studente in ogni materia
media_studente_materia = nuovo_df.groupby(['Student', 'Subject'])['Score'].mean()
print("Media dei voti per studente in ogni materia: ")
print(media_studente_materia)

