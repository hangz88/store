

import random
random.randint(0,5)
print("欢迎使用教务管理系统")
while True:
    print("1:随机点名2:随机处罚")
    num = input("请输入您的业务编号：")
    a = ["jakie","mike","jane","tony","nova"]
    if num == "1":
        index = random.randint(0,5)
        print("恭喜您:",a[index],"!")
    elif num == "2":
        choose = random.randint(0,201)
        print("恭喜您，打扫卫生",choose,"次" )
    elif num == "Q" or num== "q":
        print("系统退出，欢迎下次使用！")
        break
    else:
        print("抱歉，没有找到该业务")

