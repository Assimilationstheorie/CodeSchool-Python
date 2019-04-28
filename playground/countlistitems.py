list = [
    'a', 'b', 'a', 'c', 'b', 'd', 'a', 'b'
]

print('Die Liste = ', list)

for item in sorted(set(list)):
    count = list.count(item)
    #f-string, erlaubt Str && Int
    print( f'{item} = {count} times' )

# Ausgabe
# Die Liste =  ['a', 'b', 'a', 'c', 'b', 'd', 'a', 'b']
# a = 3 times
# b = 3 times
# c = 1 times
# d = 1 times
