import random as r

legal_x = [0,10]
legal_y = [0,10]

class Turtle:
    def __init__(self):
        self.power = 100
        self.x = r.randint(legal_x[0],legal_x[1])
        self.y = r.randint(legal_y[0],legal_y[1])

    def move(self):
        
        #随机方向并移动到新位置
        new_x = self.x + r.choice([1,2,-1,-2])
        new_y = self.y + r.choice([1,2,-1,-2])
        
        #检查是否超出场景
        if new_x < legal_x[0]:
            self.x = legal_x[0] - (new_x - legal_x[0])
        elif new_x > legal_x[1]:
            self.x = legal_x[1] - (new_x - legal_x[1])
        else:
            self.x = new_x

        if new_y < legal_y[0]:
            self.y = legal_y[0] - (new_y - legal_y[0])
        elif new_y > legal_y[1]:
            self.y = legal_y[1] - (new_y - legal_y[1])
        else:
            self.y = new_y

        #体力消耗
        self.power -= 1
        return (self.x,self.y)

    def eat(self):
        self.power += 20
        if self.power > 100:
            self.power = 100

class Fish:
    def __init__(self):
        self.power = 100
        self.x = r.randint(legal_x[0],legal_x[1])
        self.y = r.randint(legal_y[0],legal_y[1])

    def move(self):
        
        #随机方向并移动到新位置
        new_x = self.x + r.choice([1,2,-1,-2])
        new_y = self.y + r.choice([1,2,-1,-2])
        
        #检查是否超出场景
        if new_x < legal_x[0]:
            self.x = legal_x[0] - (new_x - legal_x[0])
        elif new_x > legal_x[1]:
            self.x = legal_x[1] - (new_x - legal_x[1])
        else:
            self.x = new_x

        if new_y < legal_y[0]:
            self.y = legal_y[0] - (new_y - legal_y[0])
        elif new_y > legal_y[1]:
            self.y = legal_y[1] - (new_y - legal_y[1])
        else:
            self.y = new_y

        return(self.x,self.y)
turtle = Turtle()
fish = []
for i in range(100):
    new_fish = Fish()
    fish.append(new_fish)

while True:
    if not len(fish):
        print('吃完结束')
        break
    if not turtle.power:
        print("gg")
        break

    pos = turtle.move()

    for each_fish in fish[:]:
        if each_fish.move() == pos:
            turtle.eat()
            fish.remove(each_fish)
            print("吃了鱼")


        
