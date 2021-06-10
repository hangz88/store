# 姓名：周福航
# 小组：Python自动化7组
# 声明：本代码属本人所有，未经许可，严禁
class Car:
    brand = ""
    num = 0
    color = ""
    money = 0
    site = 0

    def run(self):
        print("我驾驶着",self.brand,"飞驰在海边的公路上")

car = Car()


car.brand = "保时捷"
car.num = 4
car.color = "red"
car.money = 1000
car.site = 2

car.run()


class human:
    __name = ""
    __sex = ""
    __age = 0
    __job = ""
    __weight = ""
    def walk(self):
        print(self.__name,"吃着火锅唱着歌")


    def setname(self,name):
        self.__name = name
    def getname(self):
        return self.__name

    def setsex(self,sex):
        self.__sex = sex
    def getsex(self):
        return self.__sex

    def setjob(self,job):
        self.__job = job
    def getjob(self):
        return self.__job

    def setage(self,age):
        self.__age = age
    def getage(self):
        return self.__age

    def setweight(self,weight):
        self.__weight = weight
    def getweight(self):
        return self.__weight

    def showme(self):
        print(self.__name,"是她的名字.毫无疑问,我被",self.__name,"的",self.__sex,"性魅力所吸引，",self.__age,"的年龄正值青葱",self.__weight,"Kg的身材曼妙不已。","我要去了解她的工作",self.__job,"到底是什么,才能更好的靠近她。")



human = human()
human.setname("jane")
human.setsex("女")
human.setage(21)
human.setjob("精算师")
human.setweight("45")
human.showme()

human.walk()
