x = eval(input())
speed = 2
y = 0 #游过的总路程
z = 0 #游了多少步
while y < x:
    y +=  speed
    speed *= 0.98
    z += 1
print(z)