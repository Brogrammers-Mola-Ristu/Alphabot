import socket,time
import sqlite3,alphabot



def readDB():
    # Return the list of motion commands
    connection = sqlite3.connect("db.db")
    cursor = connection.cursor()
    res = cursor.execute("SELECT * FROM MOVIMENTO")
    movementsList_DB = res.fetchall()
    # Creation of a dict with the Command Name and Duration
    dict_DB = {}
    for m in movementsList_DB:
        dict_DB[m[0]]=m[1] # m[0]= Command Name , m[1]=duration
    return dict_DB

def runCommands(movements,bot):
    # movements = 'f,3.2; l,0.4; f,3.2;' or 'f,3.4'
    # Given one/more movement/s splits, enqueue and runs it/they 
    queue  = movements.split(";")
    # Dict of basic movements and their function
    basic_mov = {'r':bot.right , 'b':bot.backward,'l':bot.left,'f':bot.forward,'STOP':bot.stop}

    for q in queue[:-1] : 
        mov,duration = q.split(",")
        if mov in basic_mov:
            basic_mov[mov]()
            time.sleep(float(duration))
            bot.stop()

def main():
    # Creation of a TCP Server socket to run on the alphabot
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(("0.0.0.0",6000))
    s.listen()
    conn,add = s.accept()
    conn.sendall("Connected :)".encode())

    # Creation of Alphabot object --> `bot`
    bot = alphabot.AlphaBot()
    bot.stop()
    
    # Loop to recieve the commands from the Client 
    # It ends when recieves 'q' quit command
    dict_DB = readDB() 
    while True : 
        data  = conn.recv(4096)
        movements = data.decode()
        if "," in movements : 
            runCommands(movements,bot)
        if'q'in movements :
            break
        else:
            runCommands(dict_DB[movements],bot)
    s.close()

if __name__ == "__main__":
    main()