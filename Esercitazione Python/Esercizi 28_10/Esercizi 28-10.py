'''
nome = input("Inserisci il tuo nome: ")
età = int( input("Inserisci la tua età:"))
print("Ciao," + nome + "! Benvenuto in Python!")

'''

#####

#print(1 + 2)
'''
s = "Python"

print(s[0])
print(s[2])
'''

'''
saluto = "Ciao"
nome = "Alice"

messaggio = saluto + " " + nome

print(messaggio)
'''

'''
s = "Ciao,mondo"

print(len(s))
print(s.upper())
print(s.lower())
print(s.split(','))
print(s.replace("mondo", "universo"))

'''
'''
x = 5
y = 10

print(x == y)
print( x != y)
print(x > y)

'''



'''
numeri = [1, 2, 3, 4, 5]

print(numeri[0])
'''
'''
nome = input("Inserisci il tuo nome: ")
lunghezza = nome[-1]
print(lunghezza)
'''

'''
nome = input("Inserisci il tuo nome: ")
lunghezza = len(nome)
print(nome[lunghezza-1])
'''


'''
numeri = [1, 2, 3, 4, 5]

numeri.append(6)
print(numeri)

numeri.insert(2, 10)
print(numeri)

numeri.remove(4)
print(numeri)

#Rimuovere elemento di una determinata posizione
print(numeri.pop(3))
print(numeri)

numeri.sort()
print(numeri)
'''



#punto = (3,4)



'''
studente = {

  "nome": "Alice",
  "eta": "21",
  "sesso": "femmina"
}

studente["città"] = 'Roma'
print(studente)

print(studente.keys())
print(studente.values())
print(studente.items())
'''


'''
booleano = bool(int(input("Inserisci 0 o 1: ")))
intero = int(input("Inserisci un numero intero: "))
stringa = input("Inserisci un nome: ")

list = [booleano,intero,stringa]

dizionario = {
 "tipididato" : list
}

print(dizionario)
'''


'''
set1 = {1, 2, 3, 4, 5}
print(set1)

set2 = {1, 2, 2, 3, 3, 5, 6, 7}
print(set2)

set3 = set1|set2
print(set3)

set4 = set1 & set2
print(set4)

set5 = set1 - set2
print(set5)

set6 = set1 ^ set2
print(set6)
'''



# numero = int(input("Inserisci un numero: "))

# if numero % 2:
#   print("Il numero è dispari")
# else:
#   print("Il numero è pari")



#divisibile per 4 ma non per 100 o divisibile per 400


# anno = int(input("Inserire l'anno: "))

# if (anno % 4 == 0 and anno % 100 != 0) or (anno % 400 == 0):
#   print("Anno bisestile")
# else:
#   print("Anno non bisestile")



# username = "admin"
# password = "1234"

# domande = ["Quale è il tuo animale preferito?", "Qual è il tuo colore preferito?"]
# risposte = ["cane", "rosso"]

# username_input = input("Inserisci nome utente: ")
# password_input = input("Inserisci password: ")

# if username_input == username and password_input == password:
#   print("Benvenuto!")
#   scelta = int(input("Quale domanda scegli? (1 o 2): " + domande[0] + " o " + domande[1]))
#   if scelta == 1:
#     risposta_data = input("La tua risposta a: " + domande[0])
#   else: 
#     risposta_data = input("La tua risposta a: " + domande[1])
    
#   if risposta_data == risposte[0] or risposta_data == risposte[1]:
#       print("Risposta corretta! ")
#       cambio_pw = input("Vuoi cambiare la password? (si o no): ")
#       if cambio_pw == "si":
#         nuova_pw = input("Inserisci la nuova password: ")
#         print("La tua nuova password è: "+ nuova_pw)
#   else:
#      print("Risposta errata! ")
# else:
#   print("Credenziali errate")






#Esercizio su gestione di un negozio
admin_user = "admin"
admin_pw = "password"
lista_articoli = ["Pasta","Pane","Pizza"]
lista_acquisti = ["Pizza"]

domanda_utente = input("Sei un admin o un cliente?: ")
if domanda_utente == "admin":
    domanda_usr_admin = input("Inserisci nome utente: ")
    domanda_pw_admin = input("Inserisci password: ")
    if domanda_usr_admin == admin_user and domanda_pw_admin == admin_pw:
       print("Benvenuto admin!")
       scelta_attività = input( "Cosa vuoi fare? Aggiungere o rimuovere articoli dalla lista?").lower()
       if scelta_attività == "aggiungere":
         articolo_da_aggiungere = input("Inserisci articolo da aggiungere: ").lower()
         if articolo_da_aggiungere in lista_articoli:
           lista_articoli.append(articolo_da_aggiungere)
           print("Articolo aggiunto correttamente: ", lista_articoli)
         else:
            print("Articolo gia presente")
         #print(lista_articoli)
       elif scelta_attività == "rimuovere":
         print(lista_articoli)
         articolo_da_rimuovere = input("Inserisci l'articolo che vuoi rimuovere dalla lista elencata sopra: ")
         lista_articoli.remove(articolo_da_rimuovere)
    else:
       print("Credenziali errate")
else:
       utente_usr = input("Inserisci il nuovo nome utente: ") 
       utente_pw = input("Inserisci la nuova password: ")
       print("Utente registrato correttamente!")

       login_usr_utente = input("Inserisci nome utente: ")
       login_pw_utente = input("Inserisci password: ")
       if login_usr_utente == utente_usr and login_pw_utente == utente_pw:
          print("Benvenuto!")
          scelta_attività = input( "Cosa vuoi fare? Visualizzare articoli disponibili? Aggiungere o rimuovere articoli da lista acquisti?")
          if scelta_attività == "visualizzare":
            print("Gli articoli disponibili sono: ")
            print(lista_articoli)
          elif scelta_attività == "aggiungere":
            print(lista_articoli)
            articolo_da_aggiungere = input("Inserisci articolo da aggiungere tra quelli disponibili sopra elencati: ")
            
            lista_acquisti.append(articolo_da_aggiungere)
            print("Articolo aggiunto alla tua lista acquisti: ")
            print(lista_acquisti)
          elif scelta_attività == "rimuovere":
            print(lista_acquisti)
            articolo_da_rimuovere = input("Inserisci articolo da rimuovere tra la lista sopra elencata: ")
            lista_acquisti.remove(articolo_da_rimuovere)
            print("Articolo eliminato correttamente! ")
            if (len(lista_acquisti) == 0):
              print("Il carrello è vuoto!")
            else:
              print("Ecco la lista: ")
              print(lista_acquisti)
       else:
          print("Credenziali errate")




