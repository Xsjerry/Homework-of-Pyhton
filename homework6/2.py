def fib(x):
    if x == 1:
        return 1
    elif x == 2:
        return 1
    else:
        return fib(x-1) + fib(x-2)
n = int(input("Please input a number:"))
l = []
x = 1
while fib(x) < n:
    l.append(fib(x))
    x += 1
l.sort()

for i in l:
    print(i,end=',')

    
