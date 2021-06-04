# 银行的转账逻辑
def bank_translation(username,username2,password,moeny1,moeny2):
    if username not in names:
        return 1
    if password not in names[username]:
        return 2
# if int(names[username1][moeny1]) - int(moeny2) < int(0):
#   return 3
# if int(names[username1][moeny1]) - int(moeny2) >= int(0):
#   return 0


# 转账操作
def translation():
    username = input("请输入您的用户名：")
    # username2 = input("请输入对方账户名：")
    password = input("请输入您的密码：")
    # moeny2 = input("请输入转账金额：")
    if username == 1:
        print("账号不对")
    if password == 2:
        print("密码错误")
    # elif moeny2 == 3:
    #     print("钱不够")
    # elif moeny2 == 0:
    #     print("转账成功，转账",int(moeny2))