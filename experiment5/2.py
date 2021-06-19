name1 = "grade.txt"
name2 = "result.txt"
#打开文件
f1 = open(name1,"r")
f2 = open(name2,"w")
#对文件进行处理
sum = 0
l =[]
for i in f1:
    i = int(i)
    l.append(i)
    sum += i

l = sorted(l)
max = l[-1]
min = l[0]
average = sum / len(l)

f2.write("%d\n%d\n%.1f"%(max,min,average))
#关闭文件
f1.close()
f2.close()
