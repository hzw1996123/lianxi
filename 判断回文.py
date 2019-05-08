def palindrome (string):
    length = len(string)
    last = length -1
    length //= 2
    flag = 1
    for each in range(length):
        if string[each] != string[last]:
            flag = 0
        last -= 1

    if flag == 1:
        return print("是")
    else:
        return print("不是")


string = input("输入一句话：")
palindrome(string)
        
