# Module for Rotor Wheels
class Rotor:
    def __init__(self, name, wiring, rPos, nPos, rRing):
        # Setting parameters for the rotor name, forward and backward wiring,
        # initial position, notch position and the ring setting
        self.name = name
        self.fWiring = self.decode(wiring, rRing)
        self.bWiring = self.inverseDecode(wiring, rRing)
        self.rPos = rPos
        self.nPos = nPos
        self.rRing = rRing


    # Returns which Rotor Wheel Number this is
    def getName(self):
        return self.name


    # Returns Current Position of the rotor
    def getPosition(self):
        return self.rPos

    # Returns the rotor's ring setting
    def getRingSetting(self):
        return self.rRing


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
    def inverseDecode(self, wiring, rRing):
        # Inverting the string
        invWires = wiring[::1]
        # Send off the string to be decoded to an array and then returning it
        return self.decode(invWires, rRing)


    # Method for enciphering a given letter, takes the character to encipher,
    # the current rotor position, the ring setting, and which wire mapping (forward
    # or backward)
    def encipher(self, k, wireMap, rtrA):
        # We take our string character we want to encipher, and convert it to a number between
        # 0 - 25, by converting to ASCII, and subtracting 65 (We are only dealing with capitals)
        k = ord(k) - 65

        # First, we calculate the offset from the previous rotor, by taking our character
        # we are enciphering, and subtract the previous rotor's current position
        aOffset = k - rtrA.rPos
        # We then take that and add our current rotor's postion, to give us mapping input
        bInput = aOffset + self.rPos
        # Before we map, we need to subtract the Ring Setting, and constrain to between 0 and 25
        mapInput = bInput - self.rRing
        mapInputConstrained = (mapInput + 26) % 26

        # We look up our number in the wire mapping
        mapOutput = wireMap[mapInputConstrained]

        # We convert the mapping output to a number
        mapOutputChar = ord(mapOutput) - 65

        # After the mapping, we need to ADD the ring offset and constrain to 0 - 25
        mapOutput = mapOutputChar + self.rRing
        mapOutputConstrained = (mapOutput + 26) % 26

        # Because we want to Return an ASCII character, we add 65 and then convert it
        # and return the new character
        return chr(mapOutputConstrained + 65)


    # Method for enciphering a letter "forwards", or right to left through the rotor
    def forward(self, c, rtrA):
        return self.encipher(c, self.fWiring, rtrA)


    # Method for enciphering a letter "backwards", or left to right through the rotor
    def backward(self, c, rtrA):
        return self.encipher(c, self.rPos, self.bWiring, rtrA)


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
def createRotor(name, rPos, rRing):
    # Bodged Case Switch that returns a Rotor Object depending on which of the 9
    # available rotors is wanted, and will set it's initial Ring Position (rPos), 
    # the Notch Position (nPos) and the Ring Setting (rRing)
    rotorList = {
        "I": Rotor("I", "EKMFLGDQVZNTOWYHXUSPAIBRCJ", rPos, 16, rRing),
        "II": Rotor("II", "AJDKSIRUXBLHWTMCQGZNPYFVOE", rPos, 4, rRing),
        "III": Rotor("III", "BDFHJLCPRTXVZNYEIWGAKMUSQO", rPos, 21, rRing),
        "IV": Rotor("IV", "ESOVPZJAYQUIRHXLNFTGKDCMWB", rPos, 9, rRing),
        "V": Rotor("V", "VZBRGITYUPSDNHLXAWMJQOFECK", rPos, 25, rRing),
        # Rotor's 6, 7 and 8 all use 2 notch position, at 12 (M) and 25 (Z)
        "VI": Rotor("VI", "JPGVOUMFYQBENHZRDKASXLICTW", rPos, 0, rRing),
        "VII": Rotor("VII", "NZJHGRCXMYSWBOUFAIVLPEKQDT", rPos, 0, rRing),
        "VIII": Rotor("VIII", "FKQHTLXOCBJSPDZRAMEWNIUYGV", rPos, 0, rRing),
        # Default Return
        "Identity": Rotor("Identity", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", rPos, 0, rRing)
    }
    return rotorList.get(name, "Identity")
