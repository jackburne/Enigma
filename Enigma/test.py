import enigma
import argparse
import re

# def main():
#     # Creating the argument parser to handle the user inputting their settings
#     parser = argparse.ArgumentParser(description="Encrypts a text file using an implementation of the Enigma Machine")

#     # Adding the positional arguments needed to create the enigma machine
#     parser.add_argument("Rotors", help="""Select which 3 rotors, left to right, you want to be used. Given as a string of Roman Numerals: "I II III" """)
#     parser.add_argument("rPos", help="""Choose the Rotor's initial rotor position. Given as a string: "B X K" """)
#     parser.add_argument("rSet", help="""Setting the Ring Position of each Rotor. Given as a string: " V G T" """)
#     parser.add_argument("Reflector", help="""Choosing the reflector. Given as a string: "B" """)
#     parser.add_argument("Plugboard", help="""Setting Plugboard Wiring, with a max of 13 pairs. Given as a string of pairs: "AF HV ZI QF" """)
#     # Parsing Arguments into the program
#     args = parser.parse_args()

#     print("Chosen Rotors: " + args.Rotors)
#     print("Initial Rotor Positions: " + str(splitChars(args.rPos)))
#     print("Ring Settings: " + str(splitChars(args.rSet)))
#     print("Chosen Reflector: " + args.Reflector)
#     print("Plugboard Wiring: " + args.Plugboard)

#     # Creating an instance of the enigma machine, with our given settings, and doing any formatting as necerssary
#     enig = enigma.Enigma(re.split("[^a-zA-Z]", args.Rotors),
#                   splitChars(args.rPos),
#                   splitChars(args.rSet),
#                   args.Reflector,
#                   args.Plugboard)

#     print("encrypting hard coded text...")
#     print(enig.encrypt("AAAAA"))
#     print("Finished Encryption...")
    

# # Small function for handling splitting up a string into an array, based on spaces, and then
# # converting it to an ASCII value, and subbing 65, to create a value between 0 - 25
# def splitChars(rPos):
#     # First we split the string into an array based on the first occurance of any alphabetical character
#     split = re.split("[^a-zA-Z]", rPos)

#     # Then we count over each item in split, convert it to ASCII, subtract 65 to get between 0 - 25, and
#     # then replacing it's value in the array
#     for i in range(len(split)):
#         split[i] = ord(split[i]) - 65
    
#     return split

# main()



# etw = Rotor.createRotor("Identity", 0, 0)
# rtr1 = Rotor.createRotor("I", 11, 21)
# rtr2 = Rotor.createRotor("II", 24, 17)
# rtr3 = Rotor.createRotor("III", 18, 4)

# print("###BEFORE ROTATION###")
# print("Rotor 1 Position: " + str(rtr1.getPosition()))

# rtr1.turnover()

# print("###AFTER ROTATION###")
# print("Rotor 1 Position: " + str(rtr1.getPosition()))
# a = rtr1.forward("A", etw)
# b = rtr2.forward(a, rtr1)
# c = rtr3.forward(b, rtr2)

# print("Rotor 1 Output: " + a)
# print("Rotor 2 Output: " + b)
# print("Rotor 3 Output: " + c)


# print("###Testing Rotors Backwards###")

# print("###AFTER ROTATION###")
# print("Rotor 1 Position: " + str(rtr1.getPosition()))
# a = rtr3.backward("F", etw)
# b = rtr2.backward(a, rtr1)
# c = rtr1.backward(b, rtr2)

# print("Rotor 3 Output: " + a)
# print("Rotor 2 Output: " + b)
# print("Rotor 1 Output: " + c)

machine = enigma.Enigma(["I", "II", "III"], [11, 13, 15], [19, 20, 21], "B", "AB CD EF GH IJ KL MN OP")


pText = "ANDREWISTWAT"
print(machine.encrypt(pText))