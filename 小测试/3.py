x = int(input())
y = []
for i in range(1,x+1):
    if x % i == 0:
        y.append(i) 
print(y)

