x = input()
x = x.lower()
y = {}
for i in x:
    y[i] = y.get(i,0)+1
for a,b in sorted(y.items(), key=lambda item:item[1],reverse=True):
    print(a,b)
    break



