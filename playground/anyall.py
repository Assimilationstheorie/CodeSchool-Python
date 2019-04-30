data = [True, True, False]

if any(data):
    print('Etwas ist TRUE')
else:
    print('Nicht ist TRUE')

# Output: Etwas ist TRUE

if all(data):
    print('Alles ist TRUE')
else:
    print('Nicht alles ist TRUE')

# Output: Nicht alles ist TRUE
