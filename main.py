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
    return jsonify({"message" : "Creature Added Succesfully", "creatures" : creatures})

@app.route('/creatures/<string:creature_name>' , methods = ['PUT'])
def editCreature(creature_name):
    creaturesFound = []
    for creature in creatures:
        if creature['name'].lower() == creature_name.lower():
             creaturesFound.append(creature)

    if (len(creaturesFound)>0) :
        creaturesFound[0]['name'] = request.json['name']
        creaturesFound[0]['size'] = request.json['size']
        creaturesFound[0]['characteristics'] = request.json['characteristics']
        return jsonify({
            "message" : "Creature Update",
            "creature" : creaturesFound
        })
    return jsonify({"message" : "Creature Not Found"})

if __name__ == '__main__' : 
    app.run (debug = True)