#Esercizio 3
#Scrivi un sistema che prende in input una lista di numeri e stampa il quadrato di ciascun numero nella lista.


# Chiede all'utente quanti numeri desidera inserire
dimensione_lista = int(input("Quanti numeri si desidera inserire?: "))
lista_numeri = []

# Ciclo per aggiungere i numeri alla lista
for i in range(dimensione_lista):
    numero = int(input("Inserisci il numero: "))
    lista_numeri.append(numero)

# Calcola e stampa il quadrato di ciascun numero
for numero in lista_numeri:
    quadrato = numero ** 2
    print("Il quadrato di", numero, "è", quadrato)