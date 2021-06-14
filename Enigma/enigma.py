import Rotor as rtr
import Plugboard as pboard
import Reflector as rfl
import json 

# Module for creating an entire Enigma Machine. Needs to be given 5 strings: Which rotors
# to use, as Roman Numberals (i.e. ["I", "II", "III"]), Initial Rotor Positions for each rotor,
# (as [0, 15, 3]), Ring Setting (as: [3, 25, 12]), Which reflector (as: "B") and what Plugboard
# Connections (as "AF JE ZH GV")
class Enigma():
    def __init__(self, rotors, ringPos, ringSet, reflector, plugboard):
        # Creating the 3 Rotors and setting their initial Positions and Ring Settings
        self.lRotor = rtr.createRotor(rotors[0], ringPos[0], ringSet[0])
        self.mRotor = rtr.createRotor(rotors[1], ringPos[1], ringSet[1])
        self.rRotor = rtr.createRotor(rotors[2], ringPos[2], ringSet[2])

        # Creating the reflector panel
        self.reflector = rfl.createReflector(reflector)
        # Setting up Plugboard connections
        self.plugboard = pboard.Plugboard(plugboard)

        self.etw = rtr.createRotor("Identity", 0, 0)
    

    # Method for handling the rotation of the rotors
    def rotate(self):
        # First we check if the middle rotor is at it's Notch,
        # if it is, we double-step
        # if self.mRotor.isAtNotch():
        #     self.mRotor.turnover()
        #     self.lRotor.turnover()
        
        # # Next, we check if the right rotor is at it's notch
        # if self.rRotor.isAtNotch():
        #     self.mRotor.turnover()

        # # We then Rotate the right rotor
        # self.rRotor.turnover()

        if self.rRotor.isAtNotch():
            if self.mRotor.isAtNotch():
                self.lRotor.turnover()
            self.mRotor.turnover()
        self.rRotor.turnover()

    

    # Method for encrypting a single character, takes in the character as an argument 
    def encipher(self, c):
        # First we rotate the Rotors as necessary
        self.rotate()

        plugboardOutput = self.plugboard.forward(c)

        # Then we pass our plain text character through the rotors right to left
        c1 = self.rRotor.forward(plugboardOutput, self.etw)
        c2 = self.mRotor.forward(c1, self.rRotor)
        c3 = self.lRotor.forward(c2, self.mRotor)

        rotorOutput = self.etw.forward(c3, self.lRotor)

        # The new character is then reflected
        c4 = self.reflector.forward(rotorOutput)

        # Back through the rotors, left to right now, or "backwards"
        c5 = self.lRotor.backward(c4, self.etw)
        c6 = self.mRotor.backward(c5, self.lRotor)
        c7 = self.rRotor.backward(c6, self.mRotor)

        rotorOutput = self.etw.backward(c7, self.rRotor)

        # Lastly, we pass the character through the plugboard
        c8 = self.plugboard.forward(rotorOutput)

        # We then return the enciphered character
        return c8


    # Method for encrypting a whole string of charcters, returning the Cipher Text
    def encrypt(self, pText):
        # String for storing our cipher text
        cText = ""
        # Enciphering each character in our string
        for c in pText:
            cText = cText + (self.encipher(c))

        # spaced_cText = ""
        # # Once we get our cipher text back, we split it up in 5 letter blocks by looping
        # # through the cipher text,
        # for c in cText:
        #     # We add each letter to the a new string of spaced cipher text
        #     spaced_cText = spaced_cText + cText(c)
        #     # If we've gone past 5 letters,
        #     if c % 5 == 0:
        #         # We insert a space into our new text
        #         spaced_cText = spaced_cText + " "

        # Returning the encrypted cipher text
        return cText

    def getRotorPositions(self):
        positions = {
            self.rRotor.getName(): self.rRotor.getPosition(),
            self.mRotor.getName(): self.mRotor.getPosition(),
            self.lRotor.getName(): self.lRotor.getPosition()
        }
        return positions

def createEnigma(rotors, ringPos, ringSet, reflector, plugboard):
    return Enigma(rotors, ringPos, ringSet, reflector, plugboard)