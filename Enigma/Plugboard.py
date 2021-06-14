# Rotors,   Reflector, Ring Pos,   Ring Settings, plugboard
# II V III |   B C    |  7 4 19  |   12 2 20     | AF TV KO BL RW 
import re

class Plugboard:
    def __init__(self, connections):
        self.wiring = self.decodePlugboard(connections)
    

    def getWiring(self):
        return self.wiring
    

    # Method for taking in the string of letter pairs and decoding
    # them into the numerical mapping for the characters
    def decodePlugboard(self, connections):
        # First we check if we are sent an empty list of plugboard connections,
        # if we are, we just return the "Identity" Plugboard
        if connections == None or connections == "":
            return self.identityPlugboard()


        # Using some Regex, we take our single string of connections and split
        # the pairs into individual array items by splitting each pair of characters
        # regardless of case
        pairings = re.split("[^a-zA-Z]", connections)
        # We also create a mapping array that by default is the Identity Mapping
        mapping = self.identityPlugboard()
        # We also create an array to hold our "plugged characters", or which characters
        # have a plug in them
        pluggedChars = []

        # Now we validate and create the mapping using our array of pairs and the empty
        # mapping array
        # First, we check we have no more than 13 Steckered pairs supplied (Enigma never used
        # more than 13 at one time)
        if len(pairings) >= 13:
            print("Too Many Plugboard Wires!!!")
            return self.identityPlugboard()

        # We loop through each pair of characters in our pairings array
        for pair in pairings:
            # If the pair is longer than 2 (i.e. not a pair)
            if len(pair) != 2:
                # We return the identity Plugboard
                return self.identityPlugboard()
            
            # Splitting out the two characters in our current pair
            # to two seperate characters and forcing Uppercase and converting
            # to ascii
            c1 = ord(str(pair[0]).upper()) - 65
            c2 = ord(str(pair[1]).upper()) - 65

            # We then check if either of our characters already have a plug in the,
            if c1 in pluggedChars or c2 in pluggedChars:
                # If they do, we return the identity Plugboard
                return self.identityPlugboard()
            
            # We then append these characters to our list of plugged characters
            pluggedChars.append(c1)
            pluggedChars.append(c2)

            # We then update our mapping so that at location 0 (A) in the mapping array,
            # we are storing the character it is wired too, and the same for 1 (B) etc.
            mapping[c1] = c2
            mapping[c2] = c1
        
        # We then return our completed Mapping
        return mapping
    

    # Method that returns the "Identity", or default plugboard, where
    # each character is mapped to itself (i.e. no plugs)
    def identityPlugboard(self):
        mapping = []
        for i in range(26):
            mapping.append(i)

        return mapping


    # Method for finding all the plugboard letters that DO NOT have a plug in them
    def getUnpluggedChars(self, connections):
        # Empty array to store the mapping of unpluggedChars
        unpluggedChars = []
        # populating it with the "default" layout
        for i in range(26):
            unpluggedChars.append(i)

        # First we check if there are any connections at all, if not, we
        # we return the "default", or identity plugboard using the unpluggedChars list
        if "" in connections:
            return unpluggedChars
        
        # Using Regex, we then split the connections up into pairings and put each pair
        # into an array
        pairings = re.split("[^a-zA-Z]", connections)

        # We look over each plugboard pair in our array
        for pair in pairings:
            # Splitting out the two characters in our current pair
            # to two seperate characters and forcing Uppercase and converting
            # to ascii
            c1 = ord(str(pair[0]).upper()) - 65
            c2 = ord(str(pair[1]).upper()) - 65
        
            # After converting the pair characters to their ASCII characters and taking away 65
            # (to bring them down to between 0-25), we then remove those position from our array
            unpluggedChars.remove(c1)
            unpluggedChars.remove(c2)
        

        return unpluggedChars
    

    # Method for returning the wiring 
    def forward(self, c):
        # we return the contents of the wiring array, and find the look-up value
        # by taking our Uppercase character "c", converting it to it's ASCII value, and
        # subtracting 65
        return chr((self.wiring[ord(c) - 65]) + 65)


def createPlugboard(connections):    
    return Plugboard(connections)
