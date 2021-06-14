import flask
from flask import request
from flask_cors import CORS
import sys
sys.path.insert(0, './Enigma')
from Enigma import enigma


app = flask.Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def defineConfig():
    plugboardString = ""
    for pair in request.json['plugboard']:
        plugboardString = plugboardString + pair[0].upper() + pair[1].upper() + " "
    plugboardString = plugboardString.rstrip()

    reflector = request.json['reflector'].upper()

    rotorIDList = []
    rotorRingSettingList = []
    rotorPositionList = []
    for rotor in request.json['rotors']:
        rotorIDList.append(rotor['id'])
        rotorRingSettingList.append(rotor['settings'])
        rotorPositionList.append(rotor['position'])

    plaintext = request.json['plaintext'].upper()

    machine = enigma.createEnigma(rotorIDList, rotorPositionList, rotorRingSettingList, reflector, plugboardString)
    ciphertext = machine.encrypt(plaintext)

    positions = machine.getRotorPositions()

    diction = {
        "ciphertext": ciphertext,
        "positions": positions
    }

    return diction

app.run()

