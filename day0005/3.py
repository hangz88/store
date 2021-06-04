list1 = ['小明','小张','小黄','小杨']
list2 = ['小黄','小李','小王','小杨','小周']
list3 = ['小杨','小张','小吴','小冯','小周']

i = 0
while i < len(list1):
    count = 0
    j = 0
    while j < len(list1):
        if list1[i] == list1[j]:
            count = count + 1
            j = j + 1
        while j < len(list2):
            j = 0
            while j < len(list2):
                if list1[i] == list2[j]:
                    j = j + 1
                    print(list1[i])
                    i = i + 1