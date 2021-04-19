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
## 实验1:[条件P2](https://github.com/Xsjerry/Homework-of-Python/tree/main/experiment1_P2)
>> 1.判断该字符是字母字符、数字字符还是其他字符
```python
ch = input("please input a char:")
if 'a'<= ch <='z' or 'A' <= ch <= 'Z':
    print("alphabet character")
elif '1' <= ch <= '9':
    print("digital character")
else:
    print("others character")
```

>> 2.判断一个3位数是否是水仙花数。
```python
num = eval(input("please input a three-digit number:"))
a = num // 100
b = num % 100 // 10
c = num % 10
if 100 <= num <1000:
    if num == pow(a,3) + pow(b,3) + pow(c,3):
        print("true")
    else:
        print("false")
else:
    print("error")
```

>> 3.录取研究生
```python
a,b,c,d = eval(input("four scores:"))
if a>60 and b>60 and c>60 and d>60 and a+b+c+d>=370:
    print("free")
elif a>60 and b>60 and c>60 and d>60 and 340 <= a+b+c+d <=370:
    print("pay")
else:
    print("not") 
```
## 实验2：[循环结构](https://github.com/Xsjerry/Homework-of-Python/tree/main/experiment2)

>> 1.小鱼的航程
```python
# 有一只小鱼，它上午游泳150公里，下午游泳100公里，
# 晚上和周末都休息（实行双休日)，
# 假设从周x(1<=x<=7)开始算起，请问这样过了n天以后，
# 小鱼一共累计游泳了多少公里呢？
s = input()
a,b = s.split(" ")
x = int(a) #周X开始
n = int(b) #过了n天以后

distance = 0    #初始为0
for i in range(x,x+n):  #抛弃传统的周一到周七，假设周七过后是周八，以次类推，周十三就是周六，周十四就是周天
    if i % 7 != 0 and i % 7 != 6:   # 如果在n天内遇到了周末就不加，否则就加250
        distance += 250        
print(distance)
```

>> 2.Python 小球反弹
```python
#已知一球从高空落下时，每次落地后反弹至原高度的四分之一再落下。
# 编写一程序，从键盘输入整数n和m，
# 求该球从n米的高空落下后，
# 第m次落地时共经过的路程以及第m次落地后反弹的高度，
# 并输出结果。
n = int(input()) #从n米高的高空
m = int(input()) #落地m次
d = 0 #初始距离
for i in range(m):
    d += n  #下落过程加距离加n
    n *= 0.25  #n落地后的反弹的高度
    d += n  #落地后反弹距离再加 n，注意此时球在空中
#循环结束
d = d-n #因为本题要求的是球落地时的距离，所以需要减去最后一次反弹的距离
print("%.2f"%d)
print("%.2f"%n)
```
## 作业4:[循环与组合数据类型](https://github.com/Xsjerry/Homework-of-Python/tree/main/homework4)

>> 1.世界杯官网注册\
```python
# 网站注册时要求用户名只能包含字母、数字和下划线，
# 并且首字符必须是字母或下划线。
# 在计算机中编写程序判断输入的用户名是否符合该旅游网站要求，
# 如果符合，请输出“Yes”，否则输出“No”。

name = input()
if 'a' <= name[0] <= 'z' or 'A' <= name[0] <= 'Z' or name[0] == "_":
    for i in name:
        if not ('a' <= i <= 'z' or 'A' <= i <= 'Z' or i == "_" or '0' <= i <= '9'):
            x = "No"
            break
        else:
            x = "Yes"
    print(x)
else:
    print("No") 
```
>> 2.高校类型统计
```python
#列表 ls 中存储了我国 39 所 985 高校所对应的学校类型，
# 请以这个列表为数据变量，编写 代码，统计输出各类型的数量，
# 要求按类别字母顺序输出。
ls = ["Comprehensive", "Polytechnic", "Comprehensive", "Comprehensive", "Comprehensive", \

      "Comprehensive", "Comprehensive", "Comprehensive", "Comprehensive", "Comprehensive",\

      "Normal", "Polytechnic", "Comprehensive", "Polytechnic", "Comprehensive", "Comprehensive", \

      "Comprehensive", "Comprehensive", "Comprehensive","Polytechnic",\

      "Polytechnic", "Polytechnic", "Polytechnic", "Normal", "Comprehensive", \

      "Agricultural and Forestry", "Polytechnic", "Comprehensive", "Polytechnic", "Polytechnic", \

      "Polytechnic", "Comprehensive", "Polytechnic", "Comprehensive", "Comprehensive", \

      "Polytechnic", "Agricultural and Forestry", "Nationalities", "Military"]
a,c,m,p,n1,n2 = 0,0,0,0,0,0 #取各名称的首字母代表
for i in ls:
    if i[0] == "A":
        a += 1
    elif i[0] == 'C':
        c += 1
    elif i[0] == 'M':
        m += 1
    elif i[0] == 'P':
        p += 1
    else:
        if i == 'Normal':
            n1 += 1
        else:
            n2 += 1
print("Agricultural and Forestry %d"%a)
print("Comprehensive %d"%c)
print("Military %d"%m)
print("Nationalities %d"%n2)
print("Normal %d"%n1)
print("Polytechnic %d"%p)
```
>> 3.ISBN校验码判断
```python
isbn = input() #获得输入以字符串形式

num = isbn.replace('-', '') #将'-'替换为''

sum = 0 #定义初始和为0
for i in range(1,len(num)):
    if i % 2 == 0: #求偶数位
        sum += int(num[i-1])*3
    else: #求奇数位
        sum += int(num[i-1])*1

yu = sum % 10 #余数
he = 10 - yu  #稽核号
if he == 10:
    he = 0
else:
    he = 10 - yu


if he == int(num[-1]):
    print("Right")
else:
    print(isbn[0:-1]+"%d"%he)
```
## experiment3
