def isLeap(year):
    if (year%4==0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

def days(year, month):
    if month == 2:
        if isLeap(year):
            return 29
        else:
            return 28
    elif month in [4,6,9,11]:
        return 30
    else:
        return 31

x = input().split("/")

year = int(x[0])
month = int(x[1])
day = int(x[2])

sum = day
for i in range(1,month):
    sum += days(year,i) 
print(sum)




