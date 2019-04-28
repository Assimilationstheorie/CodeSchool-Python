listA = ['ListA1', 'ListA2', 'ListA3']
listB = [2,5,9]

print('Dictionary:',dict(zip(listA, listB)))
print('List:',list(zip(listA, listB)))

# Ausgabe
# Dictionary: {'ListA1': 2, 'ListA2': 5, 'ListA3': 9}
# List: [('ListA1', 2), ('ListA2', 5), ('ListA3', 9)]
