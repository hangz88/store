
name = "root"
password = "admin"
count = 0
while True:
    count = count + 1
    a = input("请输的账户:")
    b = input("请输入密码:")
    if a != name and b != password:
         print("密码输入错误，请重试")
    else:
        print("密码正确")
    if (count+ 1) >= 4:
        break







