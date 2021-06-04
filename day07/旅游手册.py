city = {
    "北京":{
        "昌平":{
            "烟袋斜街":{ "烟袋铺","钟表铺","古董店"},
            "798艺术区":{"大河画廊","千年时间画廊","亚洲艺术空间"},
                },
        "西城":{
            "北京大观园":{"潇湘馆","沁芳桥","栊翠庵"},
            "月坛公园":{"北园","南园"},
                },
        "朝阳":{
            "三里屯":{"太古里","酒吧街","使馆区"},
            "奥林匹克公园":{"鸟巢","水立方","国家体育馆"},
                 },
            }
}
def print_city(data):
    for i in data:
        print(i,"\t")




print("-------------------北京旅游指南-------------------")
print_city(city)
chose1 = input("请输入您所前往的城市：chose1>>>>>>>>")
while True:
        if chose1 in city:
            print_city(city[chose1])
            chose2 = input("请输入您前往的城区：chose2>>>>>>>")
            if chose2 in city[chose1]:
                print_city(city[chose1][chose2])
                chose3 = input("请输入您前往的区域：chose3>>>>>>>>>>>")
                if chose3 in city[chose1][chose2]:
                    print_city(city[chose1][chose2][chose3])
                # while True:
                #         a = input("请输入前往的的地点：")
                #         if a in city[chose1][chose2][chose3]:
                #             print("正在前往",a)
                #         elif a == "q" or a == "Q":
                #             print("欢迎下次使用！")
                #             break
                #             a = input("输入t或T返回第一层级")
                #             if  a =="t" or a =="T":
                #                 chose1 = input("请输入您所前往的城市：chose1>>>>>>>>")
                #                 continue
