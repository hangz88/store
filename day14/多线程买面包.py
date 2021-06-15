# 姓名：周福航
# 小组：Python自动化7组
# 声明：本代码属本人所有，未经许可，严禁商用。T_T
# 首先导入继承方法，创建厨师类，加入时间表，还有count次数，作为做面包的代码
# 然后创建顾客类，加入金钱限制，倒入继承类
# 面包数量为500时，厨师停止一秒钟 ，当顾客金钱用完时，厨师停止制作，顾客停止购买
import threading
import time
bread = 500
price = 3
count = 0
class customer(threading.Thread):
    name = ""
    num = 0
    money = 0
    def run(self) -> None:
        global bread,count,price
        while True:
            if bread > 0:
                bread = bread - 1
                self.num = self.num + 1
                self.money = self.money - price
                time.sleep(3)
                print(self.name,"抢了一个面包")
            elif bread <= 0:
                print("哎呀，面包抢光了下次再来吧")
                break
            elif self.money - price <= 0:
                print("没钱了，下次再来吧")
                break
            else:
                print(self.name,"抢了",self.num,"个面包")
                break

cm1 = customer()
cm1.name = "客户1"
cm1.money = 600

cm2 = customer()
cm2.name = "客户2"
cm2.money = 600

cm3 = customer()
cm3.name = "客户3"
cm3.money = 600

cm4 = customer()
cm4.name = "客户4"
cm3.money = 600

cm5 = customer()
cm5.name = "客户5"
cm5.money = 600

cm6 = customer()
cm6.name = "客户6"
cm6.money = 600

cm1.start()
cm2.start()
cm3.start()
cm4.start()
cm5.start()
cm6.start()

class cooker(threading.Thread):
    name = ""
    num = 0
    def run(self) -> None:
        global bread
        while True:
            if bread >= 500:
                time.sleep(3)
                print("面包数量够了，休息一下吧")
            elif bread < 500:
                self.num = self.num + 1
                time.sleep(3)
                print(self.name,"做了1个面包")
            else:
                print(self.name,"做了",self.num,"个面包")
                break

#
ck1 = cooker()
ck1.name = "面点1"
ck2 = cooker()
ck2.name = "面点2"
ck3 = cooker()
ck3.name = "面点3"
ck1.start()
ck2.start()
ck3.start()




