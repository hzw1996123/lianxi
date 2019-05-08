import random
import easygui as g

g.msgbox("猜数字游戏")
secret = random.randint(1,100)

msg = "猜数字"
title = "数字小游戏"
guess = g.integerbox(msg,title,lowerbound=1,upperbound = 100)

while True:
    if guess == secret:
        g.msgbox("ok")
        break
    else:
        if guess > secret:
            g.msgbox("大了")
        else:
            g.msgbox("小了")
        guess = g.integerbox(msg,title,lowerbound=1,upperbound = 100)

g.msgbox("结束")
