import socket
import alphabot_database

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_alphabot = ("192.168.0.147",8000)
s.connect(ip_alphabot)

data = s.recv(4096)
print(data.decode())

while True :
    command , duration  = input("Inserisci : comando , tempo di esecuzione --> ").split(",")
    if duration == "" :
        duration = "1"
    s.sendall((command+","+duration).encode())
    if command == "exit":
        break

s.close()
