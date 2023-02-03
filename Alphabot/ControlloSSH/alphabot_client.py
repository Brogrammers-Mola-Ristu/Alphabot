import socket
import ControlloSSH.alphabot_database as alphabot_database

def main():
    # Creation of a TCP Client Socket
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ip_alphabot = ("192.168.0.147",8000)
    s.connect(ip_alphabot)
    data = s.recv(4096)
    print(data.decode())

    # Loop to send the commands to the Server (Alphabot)
    # ends with command `q`
    while True :
        command  = input("Command : ")
        s.sendall((command+";").encode())
        if command == "q":
            break

    s.close()

if __name__ == "__main__":
    main()
