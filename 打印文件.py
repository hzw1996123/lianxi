def file_view(file_name,line_num):
    print("\n文件%s的前%s内容如下：\n" % (file_name,line_num))
    f = open(file_name)
    for i in range(int(line_num)):
        print(f.readline(),end = "")

    f.close()

while 1:
    file_name = input(r'请输入要打开的文件（c:\\test.txt）:')
    line_num = input("请输入需要显示该文件的前几行:")
    file_view(file_name,line_num)
