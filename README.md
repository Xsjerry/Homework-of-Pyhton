# Homework-of-Pyhton 
2021-春-应化专业-Python语言程序设计作业、

- 作业1 [编程基础和顺序结构](https://github.com/Xsjerry/Homework-of-Python/tree/main/homework1)
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
    
- 作业2 [条件](https://github.com/Xsjerry/Homework-of-Python/tree/main/homework2)
- 实验1 [条件P1](https://github.com/Xsjerry/Homework-of-Python/tree/main/experiment1)
- 作业3 [循环结构](https://github.com/Xsjerry/Homework-of-Python/tree/main/homewrok3)


