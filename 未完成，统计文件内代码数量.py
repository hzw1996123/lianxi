import easygui as g
import os

def show_result(start_dir):
    lines = 0
    total = 0
    text = ""

    for i in source_list:
        lines = source_list[i]
        total += lines
        text += '【%s】源文件%d个，源代码%d行\n' % (i,file_list[i],lines)
    title ="统计结果"
    msg = "总代码：%d,完成进度 ：%.2f %%\n离十万差%d行" % (total,total/1000,100000-total)
    g.textbox (msg,title,text)#为啥两个百分号？

def calc_code(file_name):
    lines = 0
    with open(file_name) as f:
        print("正在分析文件：%s...." % file_name)
        try:
            for each_line in f:
                lines += 1
        except UnicodeDecodeError:
                pass #遇到格式不兼容的文件忽略

        print(lines)
        return lines

def search_file(start_dir):
    os.chdir(start_dir)

    for each_file in os.listdir(os.curdir):
        ext = os.path.splitext(each_file)[1]#看不懂
        if ext in target:#target是什么？
            lines = calc_code(each_file)#统计行数
            try:
                file_list[ext] += 1
            except KeyError:
                file_list[ext] = 1
            try:
                source_list[ext] += lines
            except KeyError:
                source_list[ext] = lines


        if os.path.isdir(each_file):
            search_file(each_file)
            os.chdir(os.pardir)

target = [".py",".txt"]
file_list = {}
source_list = {}

g.msgbox("打开放代码的文件夹",'统计代码量')
path = g.diropenbox("选择您的代码库：")

search_file(path)
show_result(path)
