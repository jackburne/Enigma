class Reflector:
    def __init__(self, encoding):
        self.fWiring = self.decodeWiring(encoding)


    # Method for decoding the Wiring array into a byte array
    def decodeWiring(self, wiring):
        dWires = []

        # Looping over each character in the wiring string and pushing it to
        # our decoded array
        for char in wiring:
            dWires.append(char)

        # Returning our new array
        return dWires


    # Method for enciphering a given character using the wiring array
    def forward(self, c):
        return self.fWiring[ord(c) - 65]


# Function for creating a reflector
def createReflector(name):
    reflectorList = {
        # Regular M3 Enigma Reflectors
        "B": Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT"),
        "C": Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL"),
        # Kriegsmarine M4 "Thin" Reflectors
        "Bthin": Reflector("ENKQAUYWJICOPBLMDXZVFTHRGS"),
        "Cthin": Reflector("RDOBJNTKVEHMLFCWZAXGYIPSUQ"),
        # Default "Identity" Reflector
        "Identity": Reflector("ZYXWVUTSRQPONMLKJIHGFEDCBA")
    }

    return reflectorList.get(name, "Identity")