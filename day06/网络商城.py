print("--------","欢迎光临周福航的数码商城","--------")
trad = [["lenovo",0.5,"折券"],["iPhone" ,0.5,"折券"]]
import random
print("输入8抽取优惠券；输入9直接购物：")
num= input("请输入您的业务码:")
if num == "8":
    index = random.randint(0,1)
    print("恭喜您获得",trad[index],"*1")



elif num =="9":
    print("开始购物")
else:
    print("请输入正确折扣码")

shop = [
    ["HUAWEI P40 Pro+" ,"￥",8000],
    ["HONOR V40","￥",3500],
    ["iPhone 12 PRO","￥",7800],
    ["Lenovo Yogabook","￥",7300],
    ["MacBook Pro","￥",13000],
    ["SAMSUNG Galaxy S20","￥",6500],
]

for index,value in enumerate(shop):
    print(index,value)
salary = input("请输入您的薪资：")
salary = int(salary)
mycart = []
while True:
    for index, value in enumerate(shop):
        print(index, value)
    a = input("请输入所需商品编号：")
    if a.isdigit():
        a=int(a)
        if shop[a][2]*0.5 > salary :
            print("对不起，余额不足，请选择其他商品")
        else:
            mycart.append(shop[a])
            salary = salary - shop[a][2] or salary - shop[2][2]*0.5
            print("添加购物车成功，当前余额：￥", salary)
        pass
    elif a == "q" or a == "Q":
        print("欢迎下次使用！")
        break
    else:
        print("请输入正确商品码！")

print("本次消费记录如下:")
for index, value in enumerate(mycart):
    print(index,"", value)
print("您的余额为",salary,"元")