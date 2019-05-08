def hanoi(n,x,y,z):
    if n == 1:
        print(x,"-->",z)
    else:
        hanoi(n-1,x,z,y)#将前n-1各盘子从x移动到y
        print(x,"-->",z)#将最底下的最后一个盘子从x移动到z
        hanoi(n-1,y,x,z)#将n-1个盘子从y移动到z

        
