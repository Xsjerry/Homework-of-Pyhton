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

