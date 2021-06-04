语文= ['小明','小张','小黄','小杨']
数学 = ['小黄','小李','小王','小杨','小周']
英语 = ['小杨','小张','小吴','小冯','小周']
list1 = ['小明','小张','小黄','小杨']
list2 = ['小黄','小李','小王','小杨','小周']
list3 = ['小杨','小张','小吴','小冯','小周']

for index,value in enumerate(list1):
    if value in list1[:index]:
        continue
    else:
        print(value,"有",list1.count(value),"个人")



