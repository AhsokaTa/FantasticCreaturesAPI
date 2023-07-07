from flask import Flask, jsonify

app = Flask(__name__)

from creatures import creatures

@app.route('/')
def hello():
    return jsonify({"key":"value"})

@app.route('/creatures')
def getCreatures():
    return jsonify({"creatures" : creatures, "message":"Creature's List"})

@app.route ('/creatures/<string:creature_name>')
def getCreature(creature_name):
    creaturesFound = [creature for creature in creatures if creatures['name' == creature_name]]
    return jsonify({"creature" : creaturesFound[0]})

if __name__ == '__main__' : 
    app.run (debug = True)