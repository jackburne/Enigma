import flask
import sys
sys.path.insert(0, './Enigma')
from Enigma import enigma

from flask import request

app = flask.Flask(__name__)

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
    return ciphertext

app.run()

