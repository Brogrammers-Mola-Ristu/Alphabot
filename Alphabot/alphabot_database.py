import sqlite3

def getMovimenti():
    return [m[0] for m in movimenti]

def getAll():
    return movimenti
connection = sqlite3.connect("db.db")
cursor = connection.cursor()

res = cursor.execute("SELECT * FROM MOVIMENTO")
movimenti = res.fetchall()

print(getMovimenti())
connection.close()