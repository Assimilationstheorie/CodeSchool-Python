# :snake: Basics-Strings

### Alle Zeichen in einem String großmachen
```sh
text = "Hello World"
x = text.upper()
print(x)

# Output: HELLO WORLD
```

### Alle Zeichen in einem String kleinmachen
```sh
text = "HELLO WORLD"
x = text.lower()
print(x)

# Output: hello world
```

### Zeichen in einem String ersetzen
```sh
text = "Hello World"
txt = text.replace("H", "J")
print(txt)

# Output: Jello World
```

### Am Anfang und am Ende werden die Leerzeichen entfernt
```sh
text = " Hello World "
x = text.strip()
print(x)
```

### Ausgabe von-bis Zeichen aus einem String
```sh
x = "Hallo"
print(x[2:5])
# Output: llo
```
