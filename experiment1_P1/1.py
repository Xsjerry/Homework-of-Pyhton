import math
t = eval(input('time:'))
if t < 0.5:
    print(0)
elif t > 10:
    print(50)
else:
    print(math.ceil(t)*5) #ceil 向上取整
    


