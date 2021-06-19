f1 = open("jisuan.txt","r")
f2 = open("jieguo.txt", "w")
for i in f1.readlines():
    f2.write("%.2f\n"%eval(i))

f1.close()
f2.close()