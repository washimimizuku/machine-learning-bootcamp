for item in 'Zero to Mastery':
    print(item)

for item in [1, 2, 3, 4, 5]:
    print(item)

for item in {1, 2, 3, 4, 5}:
    print(item)

for item in (1, 2, 3, 4, 5):
    print(item)

for item in (1, 2, 3, 4, 5):
    for x in ['a', 'b', 'c']:
        print(item, x)

# Still available after the loop
print(item, x)
