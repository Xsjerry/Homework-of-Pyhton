x = input()
y=''
for i in x:
    if 'a' <= i <= 'z':
        y = y + chr(ord(i)-32)
    elif 'A' <= i <= 'Z':
        y = y + chr(ord(i)+32)
    else:
        y = y+i
print(y)
