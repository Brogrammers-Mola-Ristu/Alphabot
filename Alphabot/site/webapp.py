from flask import Flask, render_template, request
import alphabot , sqlite3 , time

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

bot = alphabot.AlphaBot()
bot.stop()
dict_DB = readDB() 
app = Flask(__name__)
print(dict_DB)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(dict_DB[request.form.get('BUTTON')])
        runCommands(dict_DB[request.form.get('BUTTON')],bot)
    elif request.method == 'GET':
        return render_template('index.html')

    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
