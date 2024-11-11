#Part 1 Scrivete un programma che genera 5 numeri casuali e li salva su un file,
#Part 2 il programma legge il file e l’utente dovrà cercare di indovinarne almeno 2 numero oppure avrà perso.
import random

def scrivi_file():
    numeri = []
    for num in range(5):
        numero = str(random.randint(1, 100))
        numeri.append(numero)

    with open("file.txt", "w") as file:
        file.write(",".join(numeri))


def leggi_file():
    with open("file.txt", "r") as file:
        contenuto = file.read()

    numeri_come_stringhe = contenuto.split(",")

    numeri = []
    for num in numeri_come_stringhe:
        numeri.append(int(num))

    return numeri



def gioco(numeri_salvati):
    numeri_indovinati = 0
    print("Prova a indovinare i numeri! (da 1 a 100)")
    
    for num in range(5):
        try:
            numero_utente = int(input("Inserisci un numero: "))
        except ValueError:
            print("Inserisci un numero valido.")
            continue

        if numero_utente in numeri_salvati:
            numeri_indovinati += 1
            numeri_salvati.remove(numero_utente)  
            print("Hai indovinato!")
        else:
            print("Sbagliato!")

    # Controlla il risultato finale
    if numeri_indovinati >= 2:
        print("Hai vinto!")
    else:
        print("Hai perso!")


scrivi_file()               
numeri = leggi_file()     
print("Numeri nel file:", numeri)  
gioco(numeri)


