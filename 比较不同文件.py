def file_compare(file1,file2):
    f1 = open(file1)
    f2 = open(file2)
    count = 0 #统计行数
    differ = [] #统计不一样的数量

    for line1 in f1:
        line1 = f2.readline()
        count += 1
        if line1 != line2:
            differ.append(count)

    f1.close()
    f2.close()
    return differ

file1 = input("输入需要比较的第一个：")
file2 = input("输入比较的第二个：")

diffe = file_compare(file1,file2 )

if len(differ) == 0:
    print("两个文件完全一样")
else:
    print('两个文件有[%d]处不同：' % len(differ))
    for each in differ:
        print('第%d行不同' % each)
        
