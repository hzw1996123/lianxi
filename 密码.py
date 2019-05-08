count = 3
password = "qwertyuiop"

while count:
    passwd = input('aanswer')
    if passwd ==password:
        print('ok')
        break
    elif"*"in passwd:
        print("密码中不能有'*'，您还有",count,"次机会！"，end="")
        continue
    else:
        print("密码中不能有'*'，您还有",count-1,"次机会！"，end="")

    count-=1
    
