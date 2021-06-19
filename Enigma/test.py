import enigma
import argparse
import re

def main():
    # escaping our regex to check for valid file paths
    validFilePath = re.compile(r'^(?:[a-z]:)?[\/\\]{0,2}(?:[.\/\\ ](?![.\/\\\n])|[^<>:\"|?*!.\/\\ \n])+$')

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
    parser.add_argument("-wf", "--writefile", help="Writes the output of the machine to a specified file, or to ciphertext.txt", type=str)
    # Parsing Arguments into the program
    args = parser.parse_args()

    # Creating an instance of the enigma machine, with our given settings, and doing any formatting as necerssary
    enig = enigma.Enigma(re.split("[^a-zA-Z]", args.Rotors),
                  splitChars(args.rPos),
                  splitChars(args.rSet),
                  args.Reflector,
                  args.Plugboard)


    # Checking if the User wanted to read in the plain text from a file
    if args.readfile != None:
        # If they do, we check we have been given a valid file path
        if validateFileName(args.readfile, validFilePath):
            # If we are, we read in the values from the text
            pText = getpText(args.readfile)

    # Running our plain text through the machine 
    cText = enig.encrypt(pText)

    # Checking if the User wanted to write the output text to a file
    if args.writefile != None:
        # Validating the output filepath
        if validateFileName(args.writefile, validFilePath):
            # Trying to write the file
            if writecText(cText, args.writefile):
                print("Written cipher text to: " + str(args.writefile))
    

# Function for getting the plain text from a text file
def getpText(pTextPath):
    # Try to open the file path given
    try:
        # Open the file and read the contents
        pText = open(pTextPath, "r")
        pTextContents = pText.read()
    except:
        print("Error Opening File...")
    finally:
        pText.close()
    
    return pTextContents


# Function for writing the cipher text to a file
def writecText(cText, cTextPath):
    try:
        # Opening a python file to write too
        cTextFile = open(cTextPath, "w")
        # Writing our cipher text
        cTextFile.write(cText)
    except:
        print("Error writing to an output file")
    finally:
        cTextFile.close()

    return True

# Function for validating that the User input file is a valid file path
def validateFileName(pathToCheck, validFilePath):
    # If our string is a valid file path, we return True, else False and print to the terminal a message
    if re.search(validFilePath, pathToCheck):
        return True
    else:
        print("Not a Valid File Path!")
        return False


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
