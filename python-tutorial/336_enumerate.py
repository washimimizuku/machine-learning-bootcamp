for i, char in enumerate('Helllooo'):
    print(i, char)

for i, char in enumerate([1, 2, 3]):
    print(i, char)

for i, char in enumerate((4, 5, 6)):
    print(i, char)

for i, char in enumerate(list(range(100))):
    if char == 50:
        print(f'Index of 50 is: {i}')
