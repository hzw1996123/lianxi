class Word(str):
    
    '''存储单词的类，定义比较单词的几种方法'''

    def __new__(cls,word):
        #必须用到__new__方法，因为str是不可变类型
        #所以在创建时将其初始化
        if " " in word:
            print ("Value contains spaces,Truncating to first space.")
            word = word[:word.index(' ')] #单词是第一个空格之前所有字符
        return str.__new__(cls,word)

    def __gt__ (self,other):
        return len(self) > len(other)
    def __it__ (self,other):
        return len(self) > len(other)
    def __ge__ (self,other):
        return len(self) > len(other)
    def __le__ (self,other):
        return len(self) > len(other)


    
