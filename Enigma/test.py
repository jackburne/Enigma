from Plugboard import Plugboard
import Rotor as rtr
import Reflector as rfl

rotor1 = rtr.createRotor("I", 25, 3)
plugboard = Plugboard("AF EJ ZY")
reflector = rfl.createReflector("B")


b = plugboard.identityPlugboard()
# c = plugboard.decodePlugboard("AF BG CH")

# print(str(plugboard.forward("E")))

print(rotor1.getName())
print(rotor1.getPosition())
d = rotor1.forward("A")
print(d)
rotor1.turnover()
print(rotor1.forward(d))

print(reflector.forward(d))
