import random
num = random.randint(1,50)
print(num)
count = 0
coin = 5000

while True :
    count = count + 1
    coin = coin - 150
    a = input("请输入您的数字:")
    a = int(a)
    if a > num:
        print("数字猜大了,消耗金币150金币剩余" ,coin,"个""您一共猜了第",count,"次")
    elif a < num:
        print("数字猜小了，消耗金币150金币剩余",coin,"个""您一共猜了第",count,"次")
    else:
        coin = coin+350
        print("恭喜您猜对了!收获金币200金币剩余",coin,"您一共猜了", count, "次")
        break
    if coin  < 0:
        print("金币用完，游戏结束")
        break
    if (count + 1) >= 100:
        break







