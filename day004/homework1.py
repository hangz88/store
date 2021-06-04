num = int(input("请输入一个数字:"))
while num != 0:
    print(num & 10)
    num = num // 10
    #结果是 0,8,10,2,0