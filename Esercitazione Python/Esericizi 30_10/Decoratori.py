# #Definizione
# def decoratore(funzione):
#     def wrapper():
#         print("Prima dell'esecuzione della funzione")
#         funzione()
#         print("Dopo l'esecuzione della funzione")
#     return wrapper


# #Utilizzo
# @decoratore
# def saluta():
#     print("Ciao!")

# saluta()





# def decoratore_con_argomenti(funzione):
#     def wrapper(*args,**kwargs):
#         print("Prima")
#         risultato = funzione(*args,**kwargs)
#         print("Dopo")
#         return risultato
#     return wrapper


# @decoratore_con_argomenti
# def somma(a,b):
#     return a + b

# print(somma(3,4))



lista_risultati = []

def salva_risultato(function):
    def wrapper(*args,**kwargs):
        risultato = function(*args,**kwargs)
        lista_risultati.append(risultato)
        return risultato
    return wrapper


@salva_risultato
def area_triangolo(base,altezza):
    return base * altezza/2 


def area_quadrato(lato):
    return lato*lato


forma_geometrica = input("Quale forma geometrica scegli per calcolare l'area? Triangolo,Quadrato,Rettangolo: " )

if forma_geometrica == "triangolo":

    base = int(input("Indicami la base: "))
    altezza = int(input("Indicami l'altezza:"))
    area_triangolo(base,altezza)
    print(lista_risultati)
elif forma_geometrica == "quadrato":

    lato = int("Inserisci il lato del quadrato")
    area_quadrato(lato)











