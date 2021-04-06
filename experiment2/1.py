# 有一只小鱼，它上午游泳150公里，下午游泳100公里，
# 晚上和周末都休息（实行双休日)，
# 假设从周x(1<=x<=7)开始算起，请问这样过了n天以后，
# 小鱼一共累计游泳了多少公里呢？
s = input()
a,b = s.split(" ")
x = int(a) #周X开始
n = int(b) #过了n天以后

distance = 0    #初始为0
for i in range(x,x+n):
    if i % 7 != 0 and i % 7 != 6:   # 如果在n天内遇到了周末就不加，否则就加250
        distance += 250        
print(distance)


