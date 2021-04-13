#ISBN码包括13位数字和4位分隔符，
#其中符号'-'就是分隔符（键盘上的减号），
#13位书号的最后一位数字为稽核号，数值范围由0至9，
#其计算方法如下：      
#(1) 用1分别乘书号的前12位数字中的奇数位，用3乘以偶数位；(去掉分隔符-后的位数，第一个数字是第1位，从奇数位开始。)
#(2)将各乘积相加，求出总和；
#(3)将总和除以10，得出余数；
#(4)将10减去余数后即为稽核号。如相减后的数值为10，稽核号则为0。
isbn = input()

num = isbn.replace('-', '')

sum = 0
for i in range(1,len(num)):
    if i % 2 == 1:
        sum += int(num[i-1])*1
    else:
        sum += int(num[i-1])*3

yu = sum % 10
he = 10 - yu
if yu == 0:
    he = 0
else:
    he = 10 - yu

if he == int(num[-1]):
    print("Right")
else:
    print(isbn[0:-1]+"%d"%he)


