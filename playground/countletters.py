message = 'Hello, World!'
stats = {
    letter: message.count(letter)
    for letter in message
}

for x in sorted(
    stats, key=stats.get, reverse=True):
    print(f'{x} = {stats[x]}')
