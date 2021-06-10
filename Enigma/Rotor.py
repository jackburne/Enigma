# Module for Rotor Wheels
class Rotor:
    def __init__(self, name, wiring, rPos, nPos, rSetting):
        # Setting parameters for the rotor name, forward and backward wiring,
        # initial position, notch position and the ring setting
        self.name = name
        self.fWiring = self.decode(wiring)
        self.bWiring = self.inverseDecode(wiring)
        self.rPos = rPos
        self.nPos = nPos
        self.rSetting = rSetting


    # Returns which Rotor Wheel Number this is
    def getName(self):
        return self.name


    # Returns Current Position of the rotor
    def getPosition(self):
        return self.rPos


    # Takes in the Rotor Wiring as a string and returns an array of that string
    def decode(self, wiring):
        # Creating an array to store the decoded string
        dWires = []
        # Looping over each character in the wiring string and pushing it to
        # our decoded array
        for char in wiring:
            dWires.append(char)

        # Returning our new array
        return dWires


    # Inverting the wiring string and then decoding it
    def inverseDecode(self, wiring):
        # Inverting the string
        invWires = wiring[::1]
        # Send off the string to be decoded to an array and then returning it
        return self.decode(invWires)


    # Method for enciphering a given letter, takes the character to encipher,
    # the current rotor position, the ring setting, and which wire mapping (forward
    # or backward)
    def encipher(self, k, rPos, rSetting, wireMap):

        # print(wireMap)
        # print("Ring Position:" + str(self.rPos))
        # print("Character At Ring Position: " + str(wireMap[self.rPos]))

        # Taking our given character and converting it to it's ASCII value - 65
        # so that it becomes a number between 0 - 25
        kc = int(ord(k) - 65)
        # Calculating the shift around the Rotor Wheel
        # by taking the current position and subbing the
        # ring setting
        rPosShift = ((rPos + rSetting) + 26) % 26
        print("Ring Position With Ring Setting Offset:" + str(rPosShift))
        # We return the character in the wiremap that is at out calculated Ring Position
        # including the ring setting (offset)
        return wireMap[kc + rPosShift]


    # Method for enciphering a letter "forwards", or right to left through the rotor
    def forward(self, c):
        return self.encipher(c, self.rPos, self.rSetting, self.fWiring)


    # Method for enciphering a letter "backwards", or left to right through the rotor
    def backward(self, c):
        return self.encipher(c, self.rPos, self.rSetting, self.bWiring)


    # Method for checking if the rotor is at it's notch position, if it is, when we
    # rotate this rotor, we also move the one to it's right
    def isAtNotch(self):
        # If we are checking the notches of rotor's 6, 7 or 8, we need to check
        # if we are at either of two notches
        if self.name == "VI" or self.name == "VII" or self.name == "VIII":
            return self.rPos == 12 or self.rPos == 25
        # Else, we are checking one of the other rotors, so we simply check the notch
        # position we were supplied when the rotor was created against it's current position
        else:
            return self.nPos == self.rPos
    

    # Method for moving the Rotor on one position
    def turnover(self):
        self.rPos = (self.rPos + 1) % 26


# Method for picking one of the 6 Rotor Wheels, and it's initial position
# ring settings
def createRotor(name, rPos, rSetting):
    # Bodged Case Switch that returns a Rotor Object depending on which of the 9
    # available rotors is wanted, and will set it's initial Ring Position (rPos), 
    # the Notch Position (nPos) and the Ring Setting (rSetting)
    rotorList = {
        "I": Rotor("I", "EKMFLGDQVZNTOWYHXUSPAIBRCJ", rPos, 16, rSetting),
        "II": Rotor("II", "AJDKSIRUXBLHWTMCQGZNPYFVOE", rPos, 4, rSetting),
        "III": Rotor("III", "BDFHJLCPRTXVZNYEIWGAKMUSQO", rPos, 21, rSetting),
        "IV": Rotor("IV", "ESOVPZJAYQUIRHXLNFTGKDCMWB", rPos, 9, rSetting),
        "V": Rotor("V", "VZBRGITYUPSDNHLXAWMJQOFECK", rPos, 25, rSetting),
        # Rotor's 6, 7 and 8 all use 2 notch position, at 12 (M) and 25 (Z)
        "VI": Rotor("VI", "JPGVOUMFYQBENHZRDKASXLICTW", rPos, 0, rSetting),
        "VII": Rotor("VII", "NZJHGRCXMYSWBOUFAIVLPEKQDT", rPos, 0, rSetting),
        "VIII": Rotor("VIII", "FKQHTLXOCBJSPDZRAMEWNIUYGV", rPos, 0, rSetting),
        # Default Return
        "Identity": Rotor("Identity", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", rPos, 0, rSetting)
    }
    return rotorList.get(name, "Identity")
