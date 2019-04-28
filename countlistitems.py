list = [
    'a', 'b', 'a', 'c', 'b', 'd', 'a', 'b'
]

for item in sorted(set(list)):
    count = list.count(item)
    print( f'{item} = {count} times' )
