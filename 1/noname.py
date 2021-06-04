#短袖的信息
id1 = 1
name1 = "短袖"
number1 = 100
color1 = "红色"
price1 = 80
size1 = "xxl"
#牛仔裤的信息
id2 = 2
name2= "牛仔裤"
number2 = 50
color2 = "黑色"
price2 = 100
size2 = "xl"
#运动服的信息
id3 = 3
name3= "运动服"
number3 = 20
color3 = "白色"
price3 = 150
size3 = "x"
#卫衣的信息
id4 = 4
name4= "卫衣"
number4 = 70
color4 = "橙色"
price4 = 80
size4 = "xxl"
#休闲裤的信息
id5 = 4
name5= "休闲裤"
number5 = 90
color5 = "白色"
price5 = 80
size5 = "xxl"
print("-----------欢迎光临周福航的网上衣橱---------")
print("----------------------------------------")
print('序号 名称 数量 颜色  价格 型号')
print(id1,"",name1,"",number1,"",color1," ",price1," ",size1)
print(id2,"",name2,"",number2,"",color2," ",price2," ",size2)
print(id3,"",name3,"",number3,"",color3," ",price3," ",size3)
print(id4,"",name4,"",number4,"",color4," ",price4," ",size4)
print(id5,"",name5,"",number5,"",color5," ",price5," ",size5)
print("-----------------------------------------")
print("总金额:""￥",(number1 * price1 + number2 * price2 + number3 * price3 + number4 * price4 + number5 * price5))