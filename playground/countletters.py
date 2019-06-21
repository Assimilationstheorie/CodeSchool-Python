message = 'Hello, World!'
stats = {
    letter: message.count(letter)
    for letter in message
}

for x in sorted(
    stats, key=stats.get, reverse=True):
    print(f'{x} = {stats[x]}')

# Ausgabe:
# l = 3
# o = 2
# H = 1
# e = 1
# , = 1
#   = 1
# W = 1
# r = 1
# d = 1
# ! = 1
