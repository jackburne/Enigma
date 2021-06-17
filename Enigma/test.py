import enigma
import argparse
import re

def main():
    # Creating the argument parser to handle the user inputting their settings
    parser = argparse.ArgumentParser(description="Encrypts a text file using an implementation of the Enigma Machine")

    # Adding the positional arguments needed to create the enigma machine
    parser.add_argument("Rotors", help="""Select which 3 rotors, left to right, you want to be used. Given as a string of Roman Numerals: "I II III" """)
    parser.add_argument("rPos", help="""Choose the Rotor's initial rotor position. Given as a string: "B X K" """)
    parser.add_argument("rSet", help="""Setting the Ring Position of each Rotor. Given as a string: " V G T" """)
    parser.add_argument("Reflector", help="""Choosing the reflector. Given as a string: "B" """)
    parser.add_argument("Plugboard", help="""Setting Plugboard Wiring, with a max of 13 pairs. Given as a string of pairs: "AF HV ZI QF" """)

    # Positional Arguments
    parser.add_argument("-rf", "--readfile", help="Reads in Cipher Text from a specified file", type=str)
    parser.add_argument("-wf", "--writefile", help="Writes the output of the machine to a specified file", type=str)
    # Parsing Arguments into the program
    args = parser.parse_args()

    print("Chosen Rotors: " + args.Rotors)
    print("Initial Rotor Positions: " + str(splitChars(args.rPos)))
    print("Ring Settings: " + str(splitChars(args.rSet)))
    print("Chosen Reflector: " + args.Reflector)
    print("Plugboard Wiring: " + args.Plugboard)

    # Creating an instance of the enigma machine, with our given settings, and doing any formatting as necerssary
    enig = enigma.Enigma(re.split("[^a-zA-Z]", args.Rotors),
                  splitChars(args.rPos),
                  splitChars(args.rSet),
                  args.Reflector,
                  args.Plugboard)

    print("encrypting hard coded text...")
    print(enig.encrypt("AAAAA"))
    print("Finished Encryption...")
    

# Small function for handling splitting up a string into an array, based on spaces, and then
# converting it to an ASCII value, and subbing 65, to create a value between 0 - 25
def splitChars(rPos):
    # First we split the string into an array based on the first occurance of any alphabetical character
    split = re.split("[^a-zA-Z]", rPos)

    # Then we count over each item in split, convert it to ASCII, subtract 65 to get between 0 - 25, and
    # then replacing it's value in the array
    for i in range(len(split)):
        split[i] = ord(split[i]) - 65
    
    return split

main()


# machine = enigma.Enigma(["I", "II", "III"], [11, 13, 15], [19, 20, 21], "B", "AB CD EF GH IJ KL MN OP")


# pText = "ANDREWISATWAT"
# print(machine.encrypt(pText))