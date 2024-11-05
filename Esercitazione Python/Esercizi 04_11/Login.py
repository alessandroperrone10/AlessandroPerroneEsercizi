def login(utente):


    while True:
            nomeutente_login = input("Inserisci il tuo nome utente: ")
            password_login = input("Inserisci la tua password: ")
            if utente.nome_utente == nomeutente_login and utente.password == password_login:
                loggato = True
                return nomeutente_login
            else:
                print("Credenziali errate!") 
                loggato = False   

            if loggato == True:
                 break
            





class Utenti:

    def __init__(self,nome_utente,password):
        self.nome_utente = nome_utente
        self.password = password
        self.punteggio = 0


utente = Utenti("alessandro","admin")


login(utente)