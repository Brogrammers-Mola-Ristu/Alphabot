import socket
import alphabot_database

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_alphabot = ("192.168.0.147", 5000)
s.connect(ip_alphabot)

data = s.recv(4096)
print(data.decode())

while True:
    command = input("Inserisci il comando ")

    s.sendall((command).encode())
    if command == "exit":
        break
s.close()
