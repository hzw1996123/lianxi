
def level():

    symbols = r'''`~!@#$%^&*()_+{}|:"<>?-=[]\;',./'''
    #三个'''和r是什么意思？
    chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    nums = '1234567890'
    g=1
    while g:
        passwd = input("输入要检查的密码组合：")
        length = len(passwd)
        while (passwd.isspace() or length == 0):
            passwd  = input("您输入的字符串为空，请重新输入：")
        if length <= 8:
            flag_len = 1
        elif 8 <length <16:
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

        while 2:
            print("您的密码安全评级为：",end="")
            if flag_len == 1 or flag_con ==1:
                print("low",end="")
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
            elif flag_con <= 2:
                print("密码太简单")
            else:
                print("ok")
                g=0
            break

level()
