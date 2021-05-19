n = int(input())
x = list(map(int,input().split(' ')))
x.sort()
count_big = 0
count_small = 0
middle = int(x[int(n/2)])
for i in x:
    if i > middle:
        count_small += 1
    elif i < middle:
        count_big += 1
if count_small == count_big:
    print(middle)
else:
    print(-1)


