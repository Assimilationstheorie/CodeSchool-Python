# Die Variablen haben den selben Wert, daher True
x = 31
y = 31

print(x == y) # Output: True
print(x is y) # Output: True

# Die Listen werden auf Referenzen geprüft. Da beide Listen auf verschiedene Adressen verweisen,
# ist zwar der Wert bei "==" True, aber da sie in verschiedenen "Orten" gespeichert werden,
# scheitert es bei "is"
a = []
b = []

print(a == b) # Output: True
print(a is b) # Output: False
