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

