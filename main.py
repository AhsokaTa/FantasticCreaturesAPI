from flask import Flask, jsonify, request

app = Flask(__name__)

from creatures import creatures

@app.route('/')
def hello():
    return jsonify({"hello":"hello world"})

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
    
@app.route('/creatures', methods =['POST'])
def addProduct():
    new_creature = {
        "name" : request.json['name'],
        "size" : request.json['size'],
        "characteristics" : request.json['characteristics']
    }
    creatures.append(new_creature)
    return jsonify({"message" : "Product Added Succesfully", "creatures" : creatures})

if __name__ == '__main__' : 
    app.run (debug = True)