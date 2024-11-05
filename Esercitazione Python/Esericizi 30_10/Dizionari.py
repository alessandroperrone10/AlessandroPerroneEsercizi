# studente = {
#     "nome" : "Alice",
#     "età" : 20,
#     "sesso" : "Femmina"
# }

# print(studente.keys())

# print(studente.values())

# print(studente.get())



booleano = bool(int(input("Inserisci 0 o 1: ")))
intero = int(input("Inserisci un numero intero: "))
stringa = input("Inserisci un nome: ")

list = [booleano,intero,stringa]

dizionario = {
 "booleano" : list[0],
 "intero" : list[1],
 "stringa" : list[2]
}

print(dizionario)