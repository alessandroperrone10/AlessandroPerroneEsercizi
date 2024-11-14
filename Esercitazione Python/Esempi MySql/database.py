import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    port = 8889,
    database="python_db"
)

# mycursor = mydb.cursor()

# #query = "CREATE DATABASE python_db"

# query = "show databases"

# mycursor.execute(query)

# for db in mycursor:
#     print(db)


#query = "CREATE TABLE utenti (id int auto_increment primary key, nome varchar(50), indirizzo varchar(50))"

mycursor = mydb.cursor()


def insert():
    query = "INSERT INTO utenti (nome, indirizzo) VALUES (%s, %s)"

    valori = [("Gianfranco","Via Gianni"), 
            ("Maria","Via Giuseppe"), 
            ("Giuseppe","Via Alessandro")]


    #mycursor.execute(query, valori)
    mycursor.executemany(query, valori)

    mydb.commit()

    print(mycursor.description, "record inseriti.")

 
def select():
    query = "SELECT * FROM utenti where nome = %s"

    valore = ("Alessandro",)

    mycursor.execute(query, valore)

    risultati = mycursor.fetchall()

    for riga in risultati:
        print(riga)



def delete():
    query = "DELETE FROM utenti WHERE nome = %s"

    valore = ("Giuseppe",)

    mycursor.execute(query, valore)

    mydb.commit()

    print(mycursor.rowcount, "record eliminati.")


def update():
    query = "UPDATE utenti SET nome = %s WHERE id = %s"

    valori = (("Giuseppe", 2),)

    mycursor.executemany(query, valori)

    mydb.commit()

    print(mycursor.rowcount, "record aggiornati.")