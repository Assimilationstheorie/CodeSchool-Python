str1 = 'strasse'
str2 = 'straße'

print(str1 == str2) # Output: False

print(
    str1.casefold() ==
    str2.casefold()
)
# Output: True
