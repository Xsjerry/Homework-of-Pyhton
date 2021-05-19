num = int(input('number:'))
l = []
for i in range(2,num):
    if num % i == 0:
        l.append(i)
if len(l) == 0:
    print("%d is prime"%num)
else:
    print(l)