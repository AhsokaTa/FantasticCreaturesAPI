from flask import Flask

app = Flask(__name__)

from creatures import creatures

@app.route('/')
def hello():
    return "Hello world"

if __name__ == '__main__' : 
    app.run (debug = True)