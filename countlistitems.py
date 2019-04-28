list = [
    'a', 'b', 'a', 'c', 'b', 'd', 'a', 'b'
]

for item in sorted(set(list)):
    count = list.count(item)
    #f-string, erlaubt Str && Int
    print( f'{item} = {count} times' )
