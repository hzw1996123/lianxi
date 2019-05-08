print('|---欢迎进入通讯录程序---|')
print("|---1:查询联系人资料---|")
print('|---2:插入新的联系人---|')
print('|---3:删除已有联系人---|')
print('|---4:退出通讯录程序---|')

contacts = dict()

while 1:
    instr = int(input('\n输入相关指令代码：'))

    if instr == 1:
        name = input('请输入联系人姓名')
        if name in contacts:
            print(name+":"+contacts[name])
        else:
            print("您输入的联系人不再通讯录中！")

    if instr == 2:
        name = input ('请输入联系人姓名：')
        if name in contacts:
            print('您输入的姓名在通讯录中已存在——》',end="")
            print(name + ":"+ contects[name])
            if input("是否修改用户资料（yes/no）") == 'yes':
                contacts[name] = input("请输入用户联系电话：")
        else:
            contacts[name] = input('请输入联系人电话:')


        if instr == 3:
            name = input("请输入联系人姓名：")
            if name in contacts:
                del(contacts[name])
            else:
                print("您输入的联系人不存在：")

            if instr == 4:
                break

print("欢迎使用")
            
