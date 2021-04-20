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






     
    