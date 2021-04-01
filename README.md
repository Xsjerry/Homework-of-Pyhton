# Homework-of-Pyhton 
2021-春-应化专业-Python语言程序设计作业、

## 作业1 [编程基础和顺序结构](https://github.com/Xsjerry/Homework-of-Python/tree/main/homework1)
>>1.Hello World程序
```python
    print("Hello World!")
```
>> 2.变量
```python
m = 100
n = 13.14
print(m)
print(n)
```
>> 3.编写程序计算下列数学表达式的结果并输出
```python
from math import sqrt
x = sqrt((3**4 + 5 * 6**7)/8)
print("{0:<9.3f}".format(x))
```
>> 4.计算圆周长和圆面积
```python
import math
r = int(input("Please enter radium:"))
c = 2 * math.pi * r
s = math.pi * r**2
print("Circumference is %.2f\nRound area is %.2f"%(c, s))
```
>> 5.3位整数逆序
```python
#num = input()
#print(num[::-1]) 使用字符串切片方法
    
num = int(input())
a = num // 100
b = num % 100 // 10
c = num % 10
print(c*100 + b*10 + a)
```
    
## 作业2 [条件](https://github.com/Xsjerry/Homework-of-Python/tree/main/homework2)
>> 1.输入整数x,y,z,判断x^3+y^3+z^3和1000的关系
```python
x,y,z = eval(input("please input three numbers:"))

if x**3 + y**3 + z**3 > 1000:
    print(x**3 + y**3 + z**3 - 1000)
    
else:
    print(x+y+z)
```
>> 2.判断一个整数是否能被7或11整除
```python
num = eval(input("number:"))
if num % 7 == 0 or num % 11 == 0:
    print("Yes")
else:
    print("No")
```
>> 3.汽车价格竞猜，单位万元。
```python
x = 25
price = eval(input("price:"))
if price > 25:
    print("high")
elif price < 25:
    print("low")
else:
    print("bingo")
```
>> 4.判断三角形
```python
a,b,c = eval(input("please input three numbers:"))
if a + b > c and a + c >b and b + c > a:
    print("true")
else:
    print("false")
```
>> 5.合法结婚年龄
```python
sex = input("Sex(F or M):")
age = eval(input("Age(1-120):"))

if sex == 'F':
    if age in range(20,121):
        print("Yes")
    elif 0<age<20:
        print("No")
    else:
        print("Error")

elif sex == 'M':
    if age in range(22,121):
        print("Yes")
    elif 0<age<22:
        print("No")
    else:
        print("Error")

else:
    print("Error")
```
>> 6.通过年份和月份，求该月天数
```python
year,month = eval(input("year,month:"))
if month in [1,3,5,7,8,10,12]:
    print(31)
elif month in [4,6,9,11]:
    print(30)
else:
    if (year%4==0 and year % 100 != 0) or year % 400 == 0:
        print(29)
    else:
        print(28) 
```
## 实验1 [条件P1](https://github.com/Xsjerry/Homework-of-Python/tree/main/experiment1)
>> 1.停车费
```python
import math
t = eval(input('time:'))
if t < 0.5:
    print(0)
elif t > 10:
    print(50)
else:
    print(math.ceil(t)*5) #ceil 向上取整
```
>> 2.骑车还是走路
```python
d = eval(input("Please input a number of distance:"))
if (50+d/4) > (d/2):
    print("Walk")
elif (50+d/4) < (d/2):
    print("Bike")
else:
    print("All")
```
>> 3.	判断三角形，并判断是何种三角形
```python
a,b,c = eval(input("please input three numbers:"))
if a+b>c and a+c>b and b+c>a:
    if a==b and b==c:
        print("equilateral triangle")
    elif a**2+b**2==c**2 or a**2 + c**2 == b**2 or b**2+c**2==a**2:
        print("right triangle")
    else:
        print("ordinary triangle")
else:
    print("false")
```

## 作业3 [循环结构](https://github.com/Xsjerry/Homework-of-Python/tree/main/homewrok3)
> 编程题
>> 1.随机密码
```python
import random
random.seed(10)
s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
x = int(input()) # 密码的长度
z = "" #定义初始密码为空
for i in range(x):
    y = random.randint(0, len(s))
    z += s[y]
print(z)
```
>> 2.循环编程题
```python
y = 0
n = 0
while y < 3:
   
    n += 1
    y += 1/(2*n-1)
    if y >= 2.99:
        break
#如果不加if条件进行判断的话，最后结果会输出57，3.00
#原因是在最后一次进行判断 y<3 后，n会+1
#所以我们要在倒数第二次循环后就推出循环   
print("n=%d,y=%.2f"%(n,y))
```
>> 3.小玉游泳
```python
x = eval(input())
speed = 2
y = 0 #游过的总路程
z = 0 #游了多少步
while y < x:
    y +=  speed
    speed *= 0.98
    z += 1
print(z)
```
>> 4.密码正确吗
```python
password = input()

if password.isdigit():
    
    for i in range(1,6):
        if int(password[i]) != (int(password[i-1])+1)**3 % 10: 
            a="wrong"
            break    
        else:
            a="right"

    print(a)
    

else:
    print("wrong")

```


