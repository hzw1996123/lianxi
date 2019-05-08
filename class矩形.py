class Ractangle:
    length = 5
    width = 4

    def setRect(self):
        print("输入长和宽")
        self.length = float(input("长："))
        self.width = float(input("宽："))

    def getRect(self):
        print("这个矩形边长是:%.2f,宽是：%.2f %" % (self.length,self.width))

    def getArea(self):
        return self.length * self.width
