a,b,c,d = eval(input("four scores:"))
if a>60 and b>60 and c>60 and d>60 and a+b+c+d>=370:
    print("free")
elif a>60 and b>60 and c>60 and d>60 and 340 <= a+b+c+d <=370:
    print("pay")
else:
    print("not") 
