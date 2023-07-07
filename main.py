from flask import Flask, jsonify

app = Flask(__name__)

from creatures import creatures

@app.route('/')
def hello():
    return jsonify({"key":"value"})

@app.route('/creatures')
def getCreatures():
    return jsonify({"creatures" : creatures, "message":"Creature's List"})

@app.route('/creatures/<string:creature_name>')
def getCreature(creature_name):
    creaturesFound = []
    for creature in creatures:
        if creature['name'].lower() == creature_name.lower():
             creaturesFound.append(creature)

    if len(creaturesFound) > 0:
        return jsonify({"creature" : creaturesFound[0]})
    else:
        return jsonify({"message" : "Creature not found"})

if __name__ == '__main__' : 
    app.run (debug = True)