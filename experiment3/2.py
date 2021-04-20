x = input()
y = ''
a = 'abcdefghijklmnopqrstuvwxyz'
b = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in x:
    if 'a' <= i <= 'z':
        y = y + chr(96+27-(ord(i)-96))
    elif 'A' <= i <= 'Z':
        y = y + chr(64+27-(ord(i)-64))
    else:
        y = y + i
print(x)
print(y)
        

