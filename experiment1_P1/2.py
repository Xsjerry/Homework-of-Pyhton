d = eval(input("Please input a number of distance:"))
if (50+d/4) > (d/2):
    print("Walk")
elif (50+d/4) < (d/2):
    print("Bike")
else:
    print("All")

