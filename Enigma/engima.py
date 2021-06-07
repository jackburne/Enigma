import Rotor as rotor
import Plugboard as pboard


class Enigma():
    def __init__(self, lRotor, mRotor, rRotor, reflector, plugboard):
        # Creating the 3 Rotors
        self.lRotor = lRotor
        self.mRotor = mRotor
        self.rRotor = rRotor

        # Creating the reflector panel
        self.reflector = reflector
        # Setting up Plugboard wiring
        self.plugboard = plugboard


