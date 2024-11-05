
#Funzione per calcolare i numeri primi
def function_numeri_primi(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

while True:
    #Input dell'utente per il range
    intervalloiniziale = int(input("Inserisci il range di inizio: "))
    intervallofinale = int(input("Inserisci il range finale: "))

    numeri_primi = []
    numeri_nonprimi = []

    for numero in range(intervalloiniziale, intervallofinale + 1):
        #Inseriamo i numeri nella lista in base al tipo
        if function_numeri_primi(numero):
            numeri_primi.append(numero)
        else:
            numeri_nonprimi.append(numero)

    print("I numeri primi dell'intervallo sono: ", numeri_primi)
    print("I numeri non primi dell'intervallo sono: ", numeri_nonprimi)

    #Chiediamo all'utente se ripetere l'operazione
    ripetere = input("Vuoi ripetere? si o no: ").lower()
    if ripetere != 'si':
        break
