
import easygui as g
user_data = {}

    
def new_user():
    prompt = "请输入用户名："
    while True:
        name = prompt
        if name in user_data:
            prompt = "此用户名已经被使用，请重新输入："
            continue
        else:
            break
        
    symbols = r'''`~!@#$%^&*()_+{}|:"<>?-=[]\;',./'''
    #三个'''和r是什么意思？
    chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    nums = '1234567890'
    g=1
    while g:
        passwd = input("输入密码：")
        length = len(passwd)
        while (passwd.isspace() or length == 0):
            passwd  = input("您输入的字符串为空，请重新输入：")
            length = len(passwd)
        if length <= 6:
            flag_len = 1
        elif 6 <length <10:
            flag_len = 2
        else:
            flag_len = 3
        flag_con = 0

        for each in passwd:
            if each in symbols:
                flag_con+=1
                break

        for each in passwd:
            if each in chars:
                flag_con+=1
                break

        for each in passwd:
            if each in nums:
                flag_con += 1
                break

        while 1:
            print("您的密码安全评级为：",end="")
            if flag_len == 1 or flag_con ==1:
                print("low")
            elif flag_len == 2 or flag_con == 2:
                print("midle")
            else :
                print("high")
                break
            break
        
        while 1:
            passwd2 = input("请重新输入密码：")
            if passwd2 != passwd:
                print("两次输入密码不一致，重新输入")
            elif flag_con < 2:
                print("密码太简单")
            else:
                print("ok")
                g=0
            break

    user_data[name] = passwd2
    print("注册成功！")
    showmenu()

    
def old_user():
    i = 3
    prompt = "请输入用户名："
    while True:
        name = input(prompt)
        if name not in user_data:
            if i == 1:
                getnew()
                break
            else:
                prompt = "您输入的用户名不存在，请重新输入："
                i-=1

           # while i:循环为什么不对？
               # prompt = "您输入的用户名不存在，请重新输入："
                #i-=1
            #getnew()
        else:
            break

    passwd = input("请输入密码：")
    pwd = user_data.get(name)
    o = 3
    while 1:
        if passwd == pwd:
            print("欢迎进入研招网")
            break
        else:
            if o > 1:
                o -= 1
                print("密码错误！")
                passwd = input("请重新输入密码：")
            else:
                print('机会用完')
                old_user()#三次机会
    
def getnew():
    choice = g.buttonbox("是否创建新用户（y/n）:",choices = ("yes","no"))
    if choice == "yes":
        new_user()
    if choice == "no":
        old_user()
    

def showmenu():
    choice = g.buttonbox("选择您想要执行的操作",choices=("新建","登录","退出"))
    choices=("新建","登录","退出")
    while 1:  
        if choice == "退出":
            break
        if choice == "新建":
            new_user()
        if choice == '登录':
            old_user()
            break

showmenu()


    
