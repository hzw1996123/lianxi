def findstr(desstr,substr):
    count = 0
    length = len(desstr)
    if substr not in desstr:
        print("在目标字符串中未找到字符串：","substr")
    else:
        for each1 in range(length - 1):
            if desstr[each1]==substr[0]:
                if desstr[each1+1]==substr[1]:
                    count += 1

        print("子字符串在目标字符串中出现%d次"% count)
#desstr = input("输入目标")
#substr = input("输入子字符串")
#函数怎么调用？为什么不能直接findstr(********,**)#
        
