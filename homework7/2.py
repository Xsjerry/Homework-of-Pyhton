f1 = open("src.txt","r")
f2 = open("dest.txt","w")

line = f1.readlines()
for i in line:
    i = i.lower()
    f2.write(i)

f1.close()
f2.close()
