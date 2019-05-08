import random
times = 8
secret = random.randint(1,50)
guess = 0
print("gues",end="")
while(guess !=secret)and(times > 0):
    temp=input()
    guess = int(temp)
    times = times - 1
    if guess == secret:
        print("ok")
    else:
        if guess > secret:
            print("big")
        else:
            print("small")
        if times > 0:
            print("try again")
        else:
            print("gg")
print("over")
