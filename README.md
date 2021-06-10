# Enigma

A python implemenation of the Enigma Machine, currently just the Enigma 1 Machine, and
the B, C and thin Reflectors

The implementation is object orientated, with a seperate module for each mechanical section of the
enigma: Rotors, Plugboard, Reflectors, and then the Enigma Machine itself

## Implementation

I have based my implementation of Enigma heavily on
Dr Mike Pound's Java version of the same program featured in a computerphile video

In his version, he works with a set of Arrays that map the values for the Rotor Wheels, Reflector and Plugboard to their numerical values between 1 - 26 (i.e. A:1, B:2, C:3 etc.). Because of how changing between strings and integers work in Java, he maps the values just as numbers:

```java
 // 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
// A B C D E F G H I J K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
```

and Java handles the conversion when you want to turn that into a Character

In my version, I store the mappings as arrays, but instead of storing the numerical value, I store the character, and where necerssary, convert that Incoming or Outgoing string to a number between 0 - 25

```python
['Y', 'R', 'U', 'H', 'Q', 'S', 'L', 'D', 'P', 'X', 'N', 'G', 'O', 'K', 'M', 'I', 'E', 'B', 'F', 'Z', 'C', 'W', 'V', 'J', 'A', 'T']
```

```python
# Taking our given character and converting it to it's ASCII value - 65
# so that it becomes a number between 0 - 25
kc = int(ord(k) - 65)
```

## TODO

- Check User Input to make sure they have entered valid settings
- Allow plain text to be read in from a file
- Allow settings to be read in from a file
- Choose between encrypting from a file, or from a string argument
- Decryption
