import os
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
    parser.add_argument("-rf", "--readfile", nargs="?", const="", help="Reads in Cipher Text from a specified file, or plaintext.txt if no file is specified")
    parser.add_argument("-wf", "--writefile", nargs="?", const="", help="Writes the output of the machine to a specified file, or to ciphertext.txt if on file is specified")
    # Parsing Arguments into the program
    args = parser.parse_args()

    # Creating an instance of the enigma machine, with our given settings, and doing any formatting as necerssary
    enig = enigma.Enigma(re.split("[^a-zA-Z]", args.Rotors),
                  splitChars(args.rPos),
                  splitChars(args.rSet),
                  args.Reflector,
                  args.Plugboard)

    # Checking if the User wanted to read in the plain text from a file
    if args.readfile == "":
        print("No Plain Text file specified, attempting to read from plaintext.txt...")
        pText = getpText('plaintext.txt')
        if pText == "":
            print("Nothing found in plaintext.txt!")

    elif args.readfile != None:
        # If they do, we check we have been given a valid file path
        # if validateFileName(args.readfile, validFilePath):
        if os.path.exists(args.readfile):
            # If we are, we read in the values from the text
            pText = getpText(args.readfile)
    
    print("Plain Text is: " + pText)

    # Running our plain text through the machine 
    cText = enig.encrypt(pText)
    print("Encrypted Plain Text!")

    if args.writefile == "":
        print("No Output file specified, attempting to write to ciphertext.txt...")
        # Trying to write the file
        if writecText(cText, 'ciphertext.txt'):
            print("Written cipher text to: " + "ciphertext.txt")
        else:
            print("Error writing file")
    # Checking if the User wanted to write the output text to a file
    elif args.writefile != None:
        # Validating the output filepath
        # if validateFileName(args.writefile, validFilePath):
        # if os.path.exists(args.writefile):
        # Trying to write the file
        if writecText(cText, args.writefile):
            print("Written cipher text to: " + str(args.writefile))
        else:
            print("Error writing to: " + str(args.writefile))
    

# Function for getting the plain text from a text file
def getpText(pTextPath):
    try:
        # Open the file and read the contents
        pText = open(pTextPath, "r")
        pTextContents = pText.read()
        pText.close()
    except FileNotFoundError:
        print("File " + pTextPath + " not found")

    return pTextContents


# Function for writing the cipher text to a file
def writecText(cText, cTextPath):
    with open(cTextPath, "w") as pTextFile:
        pTextFile.write(cText)

    return True


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
