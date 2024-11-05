# tommaso = {
#     "nome" : "tommaso",
#     "cognome" : "muraca"
# }

#print(tommaso.setdefault("via","nessuna via"))

#tommaso["via"] = "via roma"


# for chiave,valore in tommaso.items():
#     print(chiave,valore)






 #Scrivere un programma che chiede una stringa all'utente e restituisce un dizionario 
 #rappresentante la frequenza di comparsa di ciascun carattere componente la stringa.


# while True:
#     parola = input("Inserisci la parola: ")

#     dizionario = {}

#     for lettera in parola:
#         if lettera in dizionario:
#             dizionario[lettera] += 1
#         else:
#             dizionario[lettera] = 1

#     print(dizionario)


# #Alternativa
#     parola2 = "aaaaa"

#     frequenza = {}

#     for char in parola:
#         frequenza[char] = frequenza.setdefault(char,0)+1



dict1 = {"a":1,"b":2,"c":3}

dizionario = {k:v*2 for k,v in dict1.items()}

print(dizionario)




#Scrivete un prgramma che prenda i nomi degli alunni di una classe e dei voti, 
# quando l'utente scrive media il programma andrà a stampare i nomi di tutti gli alunni e per ogni alunno la media dei voti


alunni = {}
voti = []
indice = 0

while True:
    nome = input("Inserisci il nome: ")
    repeat = int(input("Quanti voti si vuole inserire?: "))

    while indice < repeat:
        voto = int(input("Inserisci il voto: "))
        voti.append(voto)
        indice += 1

    alunni[nome] = voti

 
    continuare = input("Vuoi continuare? Si, no, media: ").lower()

    if continuare == 'si':
        pass
    elif continuare == 'media':
        print("\nMedie degli alunni:")
        for nome, voti in alunni.items():
            media = sum(voti) / len(voti)
            print(f"{nome}: {media}")
        break  
    elif continuare == 'no':
        break  
