x = input("Please input a integer:")
y = x[::-1]
sumji = 0
sumou = 0
for i in range(len(x)):
    if i % 2 == 0:
        sumji += int(y[i])
    else:
        sumou += int(y[i])
   
print(sumji)
print(sumou)

if (sumji - sumou) % 11 == 0:
    print("TRUE")
else:
    print("FALSE")
    
        

