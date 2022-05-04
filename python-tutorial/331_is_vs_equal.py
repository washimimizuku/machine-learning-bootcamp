print(True == 1)
print('' == 1)
print([] == 1)
print(10 == 10.0)
print([] == [])

print(True is 1)
print('' is 1)
print([] is 1)
print(10 is 10.0)
print([] is [])

print(True is True)
print('1' is '1')
print(1 is 1)
print(10 is 10.0)
print([] is [])

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)

c = a
print(a is c)
