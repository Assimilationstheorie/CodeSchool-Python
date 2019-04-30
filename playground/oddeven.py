data = [12, 25, 34, 5, 38, 90, 43]

#ungerade
odd = []

#gerade
even = []

for d in data:
    if d % 2:
        odd.append(d)
    else:
        even.append(d)

print(f'Ungerade Nummern: {odd}')
# Output: Ungerade Nummern: [25, 5, 43]

print(f'Gerade Nummern: {even}')
# Output: Gerade Nummern: [12, 34, 38, 90]
