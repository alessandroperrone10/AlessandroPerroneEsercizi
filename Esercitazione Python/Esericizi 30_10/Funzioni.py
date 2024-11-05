# def saluta (nome):
#     print("Ciao,", nome)



# def somma(a,b):
#     risultato = a+b
#     print("La somma è: ", risultato)


# saluta("Alice")

# somma(3,5) 


# def quadrato(numero):
#     return numero * numero


# import random

# def confrontoNumero(numero):
    
#     numero_casuale = random.randint(1, 100)

#     while True:
#         if numero == numero_casuale:
#             print("Complimenti! Hai indovinato!")
#             break
#         elif numero < numero_casuale:
#             print("Il numero da indovinare è più alto.")
#             numero = int(input("Riprova! Inserisci un numero da 1 a 100: "))
#         elif numero > numero_casuale:
#             print("Il numero da indovinare è più basso.")
#             numero = int(input("Riprova! Inserisci un numero da 1 a 100: "))


# while True:
#     numero_utente = input("Inserisci un numero da 1 a 100, se non vuoi giocare digita 'esci': ")

#     if numero_utente.lower() == "esci":
#         print("Hai scelto di non giocare.")
#         break
#     else:
#         numero = int(numero_utente)
#         if 1 <= numero <= 100:
#             confrontoNumero(numero)
#         else:
#             print("Per favore, inserisci un numero valido tra 1 e 100.")











def input_utente():
    numero = int(input("Inserisci un numero: "))
    return numero


def stampa_sequenza(n):
    a = 0
    b = 1
    sequenza = []

    while a <= n:
        sequenza.append(a)
        a = b
        b = a + b
    return sequenza


numero_utente = input_utente()
sequenza_fibonacci = stampa_sequenza(numero_utente)
print ("La sequenza fino al numero: ", numero_utente, "è: ", sequenza_fibonacci)