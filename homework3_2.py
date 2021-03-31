y = 0
n = 0
while y < 3:
   
    n += 1
    y += 1/(2*n-1)
    if y >= 2.99:
        break
    
print("n=%d,y=%.2f"%(n,y))
