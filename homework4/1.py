# 网站注册时要求用户名只能包含字母、数字和下划线，
# 并且首字符必须是字母或下划线。
# 在计算机中编写程序判断输入的用户名是否符合该旅游网站要求，
# 如果符合，请输出“Yes”，否则输出“No”。

name = input()
if 'a' <= name[0] <= 'z' or 'A' <= name[0] <= 'Z' or name[0] == "_":
    for i in name:
        if not ('a' <= i <= 'z' or 'A' <= i <= 'Z' or i == "_" or '0' <= i <= '9'):
            x = "No"
            break
        else:
            x = "Yes"
    print(x)
else:
    print("No") 

