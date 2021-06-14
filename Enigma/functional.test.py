import enigma
import argparse
import re

machine = enigma.Enigma(["I", "II", "III"], [0, 15, 3], [3, 25, 12], "B", "AB CD EF GH IJ KL MN OP")

plaintext = "RYXSTXPKLBIGBKZFKIDSRVF"
ciphertext = machine.encrypt(plaintext)

print(ciphertext)
