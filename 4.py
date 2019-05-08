import random
secret = random.randint(1,20)
temp = input ("guss")
guess = int(temp)
while guess != secret:
    temp = input("again")
    guess = int ( temp )
    if guess == secret:
        print("ok")
    else:
        if guess > secret:
            print("big")
        else:
            print("small")
print("over")
