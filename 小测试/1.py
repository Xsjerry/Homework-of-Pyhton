sum = 0
z = 0
f = 0
i = int(input())
while i != 0:
    sum += i   
    if i > 0:
        z += 1
    else:
        f += 1
    i = int(input())

print(sum/(z+f))
print(z)
print(f)

