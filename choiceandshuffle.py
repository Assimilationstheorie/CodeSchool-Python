import random

lang = ["PHP", "JAVA", "HTML", "C"]

print(random.choice(lang))

# Ausgabe: Ein Item aus der Liste

random.shuffle(lang)

print(lang)

# Ausgabe: Die Liste wird zufällig sortiert
