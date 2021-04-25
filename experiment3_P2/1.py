x = input().split(' ')
for i in range(len(x)):
    for j in x[i+1:len(x)]:
        if int(x[i]) == int(j):
            del x[i]
print(len(x))