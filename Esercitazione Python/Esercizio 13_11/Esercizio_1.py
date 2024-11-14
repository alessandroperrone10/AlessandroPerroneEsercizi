#l'utente può inserire un alunno e i suoi voti in italiano e matematica, eliminare uno studente, 
# modificare un voto o uno studente, stampare tutti gli studenti e le loro medie
#il programma dovrà consentire di aggiungere non solo 2 materie ma quante materie si vogliono e quanti voti si vogliono per ogni materia


import hashlib
import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    port = 8889
)

mycursor = mydb.cursor()


query = "CREATE DATABASE IF NOT EXISTS Studenti"
mycursor.execute(query)

#mydb.close()


mydb.database = "Studenti"

query = "CREATE TABLE IF NOT EXISTS Utenti (username varchar(50) primary key, password varchar(255), isAdmin Boolean DEFAULT FALSE)"
mycursor.execute(query)

query = "CREATE Table IF NOT EXISTS Studenti (id_studente int auto_increment primary key, Nome varchar(50), username varchar(50), FOREIGN KEY (username) REFERENCES Utenti(username))"
mycursor.execute(query)


query = "CREATE TABLE IF NOT EXISTS Materie (id_materia int auto_increment primary key, Nome_Materia varchar(50))"
mycursor.execute(query)

query = "CREATE TABLE IF NOT EXISTS Voti (id_voto int auto_increment primary key, studente_id int, materia_id int, Voto int  ,FOREIGN KEY (studente_id) REFERENCES Studenti(id_studente), FOREIGN KEY (materia_id) REFERENCES Materie(id_materia))"
mycursor.execute(query) 


try:
    query = "INSERT INTO Utenti (username, password, isAdmin) VALUES (%s, %s,%s)"
    valori = ("admin", hashlib.md5("admin".encode()).hexdigest(), True)
    mycursor.execute(query, valori)
    mydb.commit()
except:
    print("Admin utente già presente.")


class Utenti():
    def hashing_pw(self,password):
        return hashlib.md5(password.encode()).hexdigest()
        
    
    # Verifica che l'input sia valido, 0<stringa<20
    def __input(self, data: str):
        if isinstance(data, str) and len(data)>0 and len(data)<20:
            return True
        else:
            return False
    

    # Verifica che le password siano concordi
    def __check_password(self, password: str, password_user:str):
            if password_user == self.hashing_pw(password):
                return True
            else:
                return False
            

    # Verifica che l'utente esite
    def __find_user(self, username):
        query = "SELECT * FROM Utenti WHERE username=%s"
        mycursor.execute(query, (username,))
        result = mycursor.fetchone()
        return result
 
    

    # def get_password(self,username):
    #     query = "SELECT password FROM Utenti WHERE username=%s"
    #     mycursor.execute(query, (username,))
    #     result = mycursor.fetchone()
    #     if result:
    #         return result[0]
    #     else:
    #         return None


    # Login, controlla l'input e la password dell'utente ed ritorna True, l'utente in caso di affermativo, altrimenti False
    def login(self):
        username = input('Username: ')
        password = input('Password: ')
        res_name = self.__input(username)
        res_pass = self.__input(password)
        if res_name == True and res_pass ==True:
            user = self.__find_user(username)
            if user!=None:
                if self.__check_password(password, user[1]):
                    return (user[0],user[2])          
        return None
    
    # Aggiunge l'untete al dizionario
    def __add_user(self, username, password):
        query = "INSERT INTO Utenti (username, password) VALUES (%s, %s)"
        valori = (username, self.hashing_pw(password))
        mycursor.execute(query, valori)
        mydb.commit()
        print(mycursor.rowcount, "Utente aggiunto.")
    
    # Registrazione, controlla l'input e la password dell'utente ed aggiunge l'utente al dizionario se validi, altrimenti False
    def register(self):
        username = input('Username: ')
        password = input('Password: ')
        nome_studente = input('Nome studente: ')
        res_name = self.__input(username)
        res_pass = self.__input(password)
        res_nome_studente = self.__input(nome_studente)
        if res_name == True and res_pass ==True and res_nome_studente == True:
            user = self.__find_user(username)
            if user==None:
                self.__add_user(username, password)
                insert_studente(nome_studente,username)
                return True
        return False




def insert_studente(nome,username):
    query = "INSERT INTO Studenti (Nome,username) VALUES (%s,%s)"
    valori = (nome,username)
    mycursor.execute(query, valori)
    mydb.commit()
    print(mycursor.rowcount, "Studente inserito.")


def insert_voto(studente_id, materia, voto):
    materia = materia.lower()

    if not check_materia(materia):
        query_materia = "INSERT INTO Materie (Nome_Materia) VALUES (%s)"
        valori_materia = (materia,)
        mycursor.execute(query_materia, valori_materia)
        mydb.commit()
    query_voto = "INSERT INTO Voti (studente_id, materia_id, Voto) VALUES (%s, (SELECT id_materia FROM Materie WHERE Nome_Materia = %s),%s)"
    valori_voti = (studente_id, materia, voto)
    mycursor.execute(query_voto, valori_voti)
    mydb.commit()


def check_materia(materia):
    query = "SELECT * FROM Materie WHERE Nome_Materia = %s"
    valori = (materia,)
    mycursor.execute(query, valori)
    return mycursor.fetchone() is not None


# def update_studente(ID,nome = None, italiano = None, matematica = None):
#     if ID_Exsist(ID):
#         if nome is not None:
#             query = "UPDATE Studenti SET nome = %s WHERE id = %s"
#             valori = (nome,ID)
#             mycursor.execute(query, valori)
#             mydb.commit()
#             print(mycursor.rowcount, "Nome utente aggiornato.")
#         elif italiano is not None:
#             query = "UPDATE Studenti SET Voto_Italiano = %s WHERE id = %s"
#             valori = (italiano,ID)
#             mycursor.execute(query, valori)
#             mydb.commit()
#             print(mycursor.rowcount, "Voto italiano aggiornato.")
#         elif matematica is not None:
#             query = "UPDATE Studenti SET Voto_Matematica = %s WHERE id = %s"
#             valori = (matematica,ID)
#             mycursor.execute(query, valori)
#             mydb.commit()
#             print(mycursor.rowcount, "Voto matematica aggiornato.")
#     else:
#         print("Studente non trovato.")


def ID_Exsist(ID):
    query = "SELECT * FROM Studenti WHERE id_studente = %s"
    valori = (ID,)
    mycursor.execute(query, valori)
    return mycursor.fetchone() is not None


def select_nome_studente(id):
    if ID_Exsist(id):
        query = "SELECT Nome FROM Studenti WHERE id_studente = %s"
        valori = (id,)
        mycursor.execute(query, valori)
        return mycursor.fetchone()
    else:
        return None

def delete_studente(id):
    if ID_Exsist(id):
        query = "DELETE FROM Studenti WHERE id_studente = %s"
        valori = (id,)
        mycursor.execute(query, valori)
        mydb.commit()
        print(mycursor.rowcount, "Utente eliminato.")
    else:
        print("Studente non trovato.")


def select_all_studenti():
    query = "SELECT * FROM Studenti"
    mycursor.execute(query)
    return mycursor.fetchall()

def select_id_utente(username):
    query = "SELECT id_studente FROM Studenti WHERE username = %s"
    valori = (username,)
    mycursor.execute(query, valori)
    return mycursor.fetchone()[0]

# SELECT avg(voti.Voto), Studenti.Nome, Materie.Nome_Materia
# FROM Voti
# INNER JOIN Studenti on Voti.studente_id = Studenti.id_studente
# INNER JOIN Materie on Voti.materia_id = Materie.id_materia
# GROUP BY Materie.Nome_Materia, Studenti.Nome;

def show_voti_alunno(id):
    if ID_Exsist(id):
        query = "SELECT Materie.Nome_Materia, Voti.Voto FROM Voti INNER JOIN Materie ON Voti.materia_id = Materie.id_materia WHERE Voti.studente_id = %s"
        valori = (id,)
        mycursor.execute(query, valori)
        voti = mycursor.fetchall() 
        for voto in voti:
            print(f"Materia: {voto[0]}, Voto: {voto[1]}")
    else:
        print("Studente non trovato.")

def show_medie_alunno(id):
    if ID_Exsist(id):
        query = " SELECT avg(voti.Voto), Materie.Nome_Materia FROM Voti INNER JOIN Studenti on Voti.studente_id = Studenti.id_studente INNER JOIN Materie on Voti.materia_id = Materie.id_materia WHERE Voti.studente_id = %s GROUP BY Materie.Nome_Materia"
        valori = (id,)
        mycursor.execute(query, valori)
        #nome_studente = select_nome_studente(id)
        dati = mycursor.fetchall()
        #print(f"Nome: {nome_studente[0]}")
        for media in dati:
             print(f"Materia : {media[1]}, Media: {media[0]}")
    else:
        print("Studente non trovato.")

def select_media_alunno_materia(id,materia):
    materia = materia.lower()
    if ID_Exsist(id):
        if check_materia(materia):
            query = "SELECT avg(Voto) from Voti WHERE studente_id = %s AND materia_id = (SELECT id_materia FROM Materie WHERE Nome_Materia = %s)"
            valori = (id,materia)
            mycursor.execute(query, valori)
            return mycursor.fetchone()
        else:
            print("Materia non trovata.")
    else:
        print("Studente non trovato.")


def select_medie_alunno(id):
    if ID_Exsist(id):
        query_materie = "SELECT Nome_Materia FROM Materie"
        mycursor.execute(query_materie)
        materie = [materia[0] for materia in mycursor.fetchall()]
        media_materie = {materia: select_media_alunno_materia(id, materia) for materia in materie}
        return media_materie,
    else:
        print("Studente non trovato.")


# def print_medie_alunno(id):
#     if ID_Exsist(id):
#         nome_studente = select_nome_studente(id)
#         medie = select_medie_alunno(id)
#         print(f"Nome: {nome_studente[0]}, Media materie: {medie}")
#     else:
#         print("Studente non trovato.")

def print_all_studenti_medie():
    query = '''SELECT  Studenti.Nome, Materie.Nome_Materia, avg(voti.Voto)
                FROM Voti
                INNER JOIN Studenti on Voti.studente_id = Studenti.id_studente
                INNER JOIN Materie on Voti.materia_id = Materie.id_materia
                GROUP BY Materie.Nome_Materia, Studenti.Nome;'''
    mycursor.execute(query)
    for row in mycursor.fetchall():
        print(row)



def menu_admin():
    while True:
        nav = input("Aggiungi voto 1, rimuovi alunno 2, visualizza media alunni 3, esci 4: ")
        if nav == '1':
            print(select_all_studenti())
            indice = int(input("Dammi l'indice dello studente per modificare il voto: "))
            nome_materia = input("Dammi il nome della materia da inserire: ")
            voto = int(input("Dammi il voto: "))
            insert_voto(indice, nome_materia, voto)
        elif nav == '2':
            pass
        elif nav == '3':
            print_all_studenti_medie()
        elif nav == '4':
            break
        else:
            print("Scelta non valida else!")

def menu_studente(username):
    id_utente = select_id_utente(username)
    show_voti_alunno(id_utente)
    show_medie_alunno(id_utente)



utenti = Utenti()

while True:
    nav = input("Seleziona l'opzione: 1. Login, 2. Registrazione, 3. Esci: ")
    if nav == '1':
        check_login = utenti.login()
        if check_login != None:
            print(f"Benvenuto {check_login[0]}!")
            if check_login[1] == True:
                menu_admin()
            else:
                menu_studente(check_login[0])
        else:
            print("Credenziali errate!")
    elif nav == '2':
        check_registrazione = utenti.register()
        if check_registrazione == True:
            print("Registrazione avvenuta con successo!")
        else:
            print("Utente già registrato!")
    elif nav == '3':
        break






