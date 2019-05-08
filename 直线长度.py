import math

class Point():
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def getY(self):
        return self.y

    def getX(self):
        return self.x

class Line():
    def __init__(self,p1,p2):
        self.x = p1.getX() - p2.getX()
        self.y = p1.getY() - p2.getY()
        self.len = math.sqrt(self.x*self.x+self.y*self.y)

    def getLen(self):
        return self.len
    
