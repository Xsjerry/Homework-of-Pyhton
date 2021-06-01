def mySum(a, n):
    sum1 = 0
    sum2 = 0
    for i in range(1,n+1):
        sum1 += 10**(i-1)*a
        sum2 += sum1
    return sum2
x = input()
x = x.split(',')
a = int(x[0])
n = int(x[1])
print(mySum(a, n))
