import sqlite3

connection = sqlite3.connect("movimenti.db")
cursor = connection.cursor()

res = cursor.execute("SELECT * FROM MOVIMENTO")
movimenti = res.fetchall()
connection.close()

diz = {}
for movimento in movimenti:
    diz[movimento[0]] = movimento[1]

comando = ""
while comando != "quit":
    comando = input("Inserisci il comando: ")
    if comando in diz:
        print("azione: ", diz[comando])
    else:
        print("comando non trovato")
