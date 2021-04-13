#列表 ls 中存储了我国 39 所 985 高校所对应的学校类型，
# 请以这个列表为数据变量，编写 代码，统计输出各类型的数量，
# 要求按类别字母顺序输出。
ls = ["Comprehensive", "Polytechnic", "Comprehensive", "Comprehensive", "Comprehensive", \

      "Comprehensive", "Comprehensive", "Comprehensive", "Comprehensive", "Comprehensive",\

      "Normal", "Polytechnic", "Comprehensive", "Polytechnic", "Comprehensive", "Comprehensive", \

      "Comprehensive", "Comprehensive", "Comprehensive","Polytechnic",\

      "Polytechnic", "Polytechnic", "Polytechnic", "Normal", "Comprehensive", \

      "Agricultural and Forestry", "Polytechnic", "Comprehensive", "Polytechnic", "Polytechnic", \

      "Polytechnic", "Comprehensive", "Polytechnic", "Comprehensive", "Comprehensive", \

      "Polytechnic", "Agricultural and Forestry", "Nationalities", "Military"]
a,c,m,p,n1,n2 = 0,0,0,0,0,0
for i in ls:
    if i[0] == "A":
        a += 1
    elif i[0] == 'C':
        c += 1
    elif i[0] == 'M':
        m += 1
    elif i[0] == 'P':
        p += 1
    else:
        if i == 'Normal':
            n1 += 1
        else:
            n2 += 1
print("Agricultural and Forestry %d"%a)
print("Comprehensive %d"%c)
print("Military %d"%m)
print("Nationalities %d"%n2)
print("Normal %d"%n1)
print("Polytechnic %d"%p)