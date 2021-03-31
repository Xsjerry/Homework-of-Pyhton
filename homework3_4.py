password = input()

while password.isdigit():
    
    for i in range(1,6):
        if int(password[i]) == int(str((int(password[i-1])+1)**3)[-1]):
            a="right"    
        else:
            a="wrong"

    print(a)
    break

else:
    print("wrong")






     
    