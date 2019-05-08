def mfun(*param, bace = 3):
    result = 0
    for each in param:
        result += each

    result *=bace
    print("结果是：", result)
