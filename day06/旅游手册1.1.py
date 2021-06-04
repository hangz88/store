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
chose1 = input("请输入省市：chose1>>>>>>>>")
while True:
        if chose1 in city:
            print_city(city[chose1])
            chose2 = input("请输入县区：chose2>>>>>>>>>>>>>")
            if chose2 in city[chose1]:
                print_city(city[chose1][chose2])
                chose3 = input("请输入景区：chose3>>>>>>>>>>>>")
                if chose3 in city[chose1][chose2]:
                    print_city(city[chose1][chose2][chose3])
                    chose4 = input("请输入景点，或输入0关闭系统：chose4>>>>>>>>>>.")
                    if chose4 in city[chose1][chose2][chose3]:
                        print("正在前往",chose4)
                    elif chose4 == "0":
                        print("欢迎下次使用！")
                        break





