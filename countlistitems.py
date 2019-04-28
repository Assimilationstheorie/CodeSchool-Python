list = [
    'a', 'b', 'a', 'c', 'b', 'd', 'a', 'b', 'f', 'd'
]

for item in sorted(set(list)):
    count = list.count(item)
    print item, '=', count, 'times'
