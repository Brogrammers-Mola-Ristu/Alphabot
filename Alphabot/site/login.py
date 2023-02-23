from flask import Flask, render_template, redirect, url_for, request
import sqlite3,time,alphabot
import hashlib , random 

app = Flask(__name__)
bot = alphabot.AlphaBot()
bot.stop()
site_access = ''.join(random.choice('qwertyuiop1a2s3d4f5gh6j7k8l90')for i in range(20))
print(site_access)

def readDB():
    # Return the list of motion commands
    connection = sqlite3.connect("movements.db")
    cursor = connection.cursor()
    res = cursor.execute("SELECT * FROM MOVIMENTI")
    movementsList_DB = res.fetchall()
    connection.close()
    
    # Creation of a dict with the Command Name and Duration
    dict_DB = {}
    for m in movementsList_DB:
        dict_DB[m[0]]=m[1] # m[0]= Command Name , m[1]=duration
    
    return dict_DB

dict_DB = readDB() 

def runCommands(movements,bot):
    # movements = 'f,3.2; l,0.4; f,3.2;' or 'f,3.4'
    # Given one/more movement/s splits, enqueue and runs it/they 
    queue  = movements.split(";")
    # Dict of basic movements and their function
    basic_mov = {'r':bot.right , 'b':bot.backward,'l':bot.left,'f':bot.forward}

    for q in queue[:-1] : 
        mov,duration = q.split(",")
        if mov in basic_mov:
            basic_mov[mov]()
            time.sleep(float(duration))
            bot.stop()


def validate(username, password):
    completion = False
    con = sqlite3.connect('./user.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM Utenti")
    rows = cur.fetchall()
    for row in rows:
        dbUser = row[0]
        dbPass = row[1]
        print(dbPass)
        if dbUser==username:
            completion=check_password(dbPass, password)
    return completion

def check_password(hashed_password, user_password):
    return hashed_password == user_password

@app.route('/', methods=['GET', 'POST'])
def login():
    
    error = None
    if request.method == 'POST':
        username = request.form.get('user')
        print(username)
        password = request.form.get('psw')
        password = hashlib.sha256(password.encode()).hexdigest()
        print(password)
        completion = validate(username, password)
        
        if completion == False:
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('webapp'))

    return render_template('index.html', error=error)



@app.route(f'/{site_access}' , methods=['GET', 'POST'])

def webapp():
    if request.method == 'POST' :
        print(dict_DB[request.form.get('BUTTON')])
        runCommands(dict_DB[request.form.get('BUTTON')],bot)
    elif request.method == 'GET':
        return render_template('webapp.html')
    return render_template('webapp.html')
    

if __name__== "__main__":
    app.run(debug=True, host='0.0.0.0')