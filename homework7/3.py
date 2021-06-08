f1 = open('movie.txt',"r",encoding="utf-8")
f2 = open('out.txt',"w")
lines = f1.readlines()
for i in lines[1:]:
    i = i.replace("\n","")
    i = i.split("\t")
    if int(i[-1].lstrip()) <= 90:
        f2.write(i[0]+"\n")

f1.close()
f2.close()
    
    
    



    


    
    

