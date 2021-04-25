x = input('numbers:').split(',')
y = [eval(i) for i in x]
l = []
for i in range(len(y)):
    for j in range(i+1,len(y)):
        if int(y[i]+y[j]) == 9:
            a,b=min((y[i],y[j])),max((y[i],y[j]))
            l.append((a,b))

l = list(set(l))
l.sort()

print(l,sep='')
