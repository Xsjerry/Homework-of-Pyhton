import random
random.seed(10)
s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
x = int(input()) # 密码的长度
z = "" #定义初始密码为空
for i in range(x):
    y = random.randint(0, len(s))
    z += s[y]
print(z)


