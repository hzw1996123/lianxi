def count(*param):
    length = len(param)
    for i in range(length):
        letters = 0
        space = 0
        digit = 0
        others = 0
        for each in param[i]:
            print(each)
            if each.isalpha():
                letters += 1
            elif each.isdigit():
                digit += 1
            elif each == " ":
                space += 1
            else:
                others += 1

                
        print("digit:",digit   ,"letters:",letters,"space:",space,"others:",others)
        print(each)
        

count(" j jjj jnjij898hnuiniad"," jsnandjianudn8888888888888888888888888")
