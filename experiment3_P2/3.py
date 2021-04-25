x = input()
y = input().split()
y = [eval(i) for i in y]
d = {}

for i in y:
    d[i] = d.get(i,0)+1

maxtime = max(d.values())
l = list(d.items())
l.sort()

for i in l:
    if i[1] == maxtime:
        print(i[0],i[1])
