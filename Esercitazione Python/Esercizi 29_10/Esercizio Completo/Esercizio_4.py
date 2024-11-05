# Chiediamo all'utente i numeri
lista_numeri = []

while True:
    numeri_utente = input("Inserisci un numero, se vuoi fermarti digita stop: ")

    if numeri_utente == "":
        print("La lista è vuota")   
    elif numeri_utente.lower() == "stop":
        break
    else:
        lista_numeri.append(int(numeri_utente))


# Trova il numero massimo nella lista usando un ciclo for
massimo = lista_numeri[0]
for numero in lista_numeri:
    if numero > massimo:
        massimo = numero

# Conta il numero di elementi nella lista usando un ciclo while
conteggio = 0
while conteggio < len(lista_numeri):
    conteggio += 1
    
# Stampa il numero massimo e il numero di elementi nella lista
print("Numero massimo: ", massimo)
print("Numero di elementi nella lista: ", conteggio)
