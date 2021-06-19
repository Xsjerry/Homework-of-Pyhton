import math
def sushu(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False

n = eval(input())
for i in range(2, int(math.sqrt(n)+1)):
    if (n % i == 0) and sushu(i) and sushu(n/i):
        x = "JH"+str(int(n/i))+str(int(i))
        break
    else:
        x = "error" 
print(x)



    