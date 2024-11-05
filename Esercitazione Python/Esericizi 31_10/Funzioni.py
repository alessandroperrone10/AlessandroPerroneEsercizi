# def funzione(*argomento,**argomenti2):
#     print(argomento[0])
#     print(argomenti2)

# funzione(11,2,4, num1 = 11, num2 = 2, num3 = 4)

# #Utilizzo di una variabile globale in funzione locale
# variabile1 = 10

# def funzione():
#     global variabile1
#     variabile1 = 11


# print(variabile1)
# funzione()
# print(variabile1)




# def triplica(a):
#     return a*3

# lista = [1,2,3,4,5]

# # listaT = []

# # for num in lista:
# #     listaT.append(triplica(num))

# listaT = list(map(triplica, lista))

# print(listaT)


# lista = [1,2,3,4,5]

# def numero_p(n):
#     return n%2 == 0

# listaP = list(filter(numero_p,lista))

# print(listaP)





#Scrivere un programma che utilizza una funzione che accetta come parametro una stringa passata dall'utente e restituisce in risposta se è palindroma o no



# def palindromo(frase):
   
#    frase = frase.replace(" ","").lower()
#    frase_inversa = frase[::-1]

#    if frase == frase_inversa:
#       return True
#    else:
#       return False


# while True:
#     frase = input("Inserisci la frase: ")

#     risultato = palindromo(frase)

#     if risultato == True:
#         print("La frase è palindroma")
#     else:
#         print("La frase non è palindroma")










    
