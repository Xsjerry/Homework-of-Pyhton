'''   num = input()
      print(num[::-1]) 
'''
num = int(input())
a = num // 100
b = num % 100 // 10
c = num % 10
print(c*100 + b*10 + a)

