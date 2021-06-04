import random
num  = input("请输入您的分数：")
num = int(num)
if num >= 90 and num <= 100 :
    print("太棒了！A+")
if num >= 80 and num <90 :
    print("真不错。good!")
if num >=70 and num < 80 :
    print("还可以。not bad.")
if num >=60 and num < 70:
    print("快点补习！c-")
if num >= 0 and num< 60 :
    print("好好学习")
else:
    print("非法输入")
