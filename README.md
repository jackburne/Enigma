# Enigma

A python implemenation of the Enigma Machine, currently just the Enigma 1 Machine, and
the B, C and thin Reflectors

The implementation is object orientated, with a seperate module for each mechanical section of the
enigma: Rotors, Plugboard, Reflectors, and then the Enigma Machine itself

## Usage

There are two ways to use this Enigma machine: importing it into your project, and parsing it strings and settings. You can then call the Enigma.encrypt() method with a string you want to encrypt. It will remove any special characters, capitlise all the alphabetical letters, and if the program finds a ".", it will convert it to
the word "STOP", as would be done with the original machine.

Once it encrypts text, it will obfusticate the text by spacing it every 5 letters, again similar to the original machine, and procedures would do.

```python
import enigma

# Settings given as strings in this order: Rotors, Rotor start positions, Ring Settings, Reflector, Plugboard Connections
machine = enigma.Enigma("I II III", "A B C", "D E F", "B", "AB CD EF GH")

# Returns a string of encrypted text
ciphertext = machine.encrypt("string to encrypt with special characters #!&*^*&%")
```

The other way to use this machine is as a standalone program, using the "front end".

To do this, simply pull or download the repo, and call the "####.py" file, with a minimum of the initial machine settings (Chosen Rotors, Initial starting positions, Ring settings, Reflector, Plugboard Connections), with the option of adding a txt file to read from, and/or an file to write the cipher text to:

```bash
# Minimum possible settings to use, will by default attempt to read from "plaintext.txt", and write to "ciphertext.txt"
$> python test.py "I II III" "A B C" "D E F" "B" "AB CD EF GH IJ"

# Same initial setup, using different rotors and start settings, but also parsing in the -rf and -wf flags to specify a file to read and a file to write to
$> python test.py "VI V IV" "Z Y X" "W V U" "C" "ZY XW VU TS" -rf helloworld.txt -wf encryptedtext.txt
```

## Implementation

I have based my implementation of Enigma heavily on
Dr Mike Pound's Java version of the same program featured in a computerphile video


## Rotor Wheels
```
# Pseudo Code for Rotor Wheel Encoding
Function RtrB (Out_RtrA, WireMap, RtrA){
    offset = Out_RtrA - Position of RtrA
    Input to RtrB = offset + Position of RtrB
    character to map = Input to RtrB - RtrB Ring Setting

    MAP Character

    return Mapped Character - RtrB Ring Setting
}
```

