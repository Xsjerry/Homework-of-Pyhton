n = int(input())
x = input().split(' ')
d = {}
for i in x:
    d[i] = d.get(i,0)+1
    print('%d'%d[i],end=' ')
