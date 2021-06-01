def sumThree(n):
    sum = 0
    for i in range(1,int(n)+1,2):
        for j in range(len(str(i))):
            if str(i)[j] == '3':
                sum += 1
    return sum


n = input("number:")
print(sumThree(n))
