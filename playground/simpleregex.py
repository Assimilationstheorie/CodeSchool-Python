import re
text = "Guten Morgen, Freunde"
hallo = re.sub("Morgen", "Abend", text)
print(hallo)

# Ausgabe
# Guten Abend, Freunde
