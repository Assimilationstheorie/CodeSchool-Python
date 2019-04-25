from random import randint

# Der Datentyp set ist ein sogenannter "collection"-Typ. Ein set enthält eine ungeordnete Sammlung von einmaligen und unveränderlichen Elementen. Ein Element kann in einem set-Objekt nicht mehrmals vorkommen
data = set()
# Setzt die Variable n auf 0
n = 0
# Solange n unter 20 ist...
while n < 20:
    # Die Variable kriegt eine zufällige Zahl zwischen 0 und 100
    r = randint(0, 100)
    # Erhöht die n-Variable um 1+
    n += 1
    # Die Variable "data" kriegt mit der Funtion add() eine zufällige Zahl zugewiesen
    data.add(r)
# Gibt die Länge der data-Variable aus
print(len(data))
# Gibt alle Elemente der data-Variable aus
print(data)
