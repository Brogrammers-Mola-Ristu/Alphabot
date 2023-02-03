import flask,sqlite3

app = flask.Flask(__name__)

def validate(username,psw):
    completition = False
    conn = sq