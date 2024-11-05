#Esercizio Precedente
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



#Esercizio Registrazione e Login
def registrazione():
    nome_utente = input("Inserisci il nome utente: ")
    password = input("Inserisci la password: ")

    return nome_utente,password
    


def login(utente,password):
    nome_login = input("Quale è il tuo nome utente?:  ")
    password_login = input("Quale è la tua password?:  ")


    if utente == nome_login and password_login == password:
        utente_loggato = True
        #print("Benvenuto! ")
        return utente_loggato
    else:
        print("Credenziali errate! ")
        utente_non_loggato = False
        return utente_non_loggato


def menu():
    print("Benvenuto ", credenziali[0], " !")
    numero_utente = input_utente()
    sequenza_fibonacci = stampa_sequenza(numero_utente)
    print ("La sequenza fino al numero: ", numero_utente, "è: ", sequenza_fibonacci)


credenziali = registrazione()

while True:
    loggato = login(credenziali[0],credenziali[1])
    if loggato == True:
        menu()
        break

