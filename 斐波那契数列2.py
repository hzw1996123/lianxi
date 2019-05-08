def fab(n):
    if n < 1:
        print("输入错误")
        return -1

    if n == 1 or n == 2:
        return 1
    else:
        return fab(n-1)+fab(n-2)
