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