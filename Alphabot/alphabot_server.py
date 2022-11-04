import socket,time
import sqlite3,alphabot

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("0.0.0.0",8000))
s.listen()
bot = alphabot.AlphaBot()
bot.stop()
connection = sqlite3.connect("db.db")
cursor = connection.cursor()

res = cursor.execute("SELECT * FROM MOVIMENTO")
movimenti = res.fetchall()

comandi  = {}

conn,address = s.accept()
conn.sendall("Connessione Avvenuta".encode())


while True : 
    data = conn.recv(4096)
    action = data.decode().split(",")
    print(action)
    if len(action)>=1:
        movement,duration = action[0],float(action[1])
    else : duration = 1


    if movement in comandi:
        comandi[movement]()
        time.sleep(duration)
        bot.stop()

    else : break

s.close()   

