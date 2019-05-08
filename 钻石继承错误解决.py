class A():
    def __init__ (self):
        print("进入A")
        print("离开A")

class B(A):
    def __init__(self):
        print('进入B')
        super().__init__()
        print("离开B")

class C(A):
    def __init__ (self):
        print("进入C")
        super().__init__()
        print("离开C")

class D(C,B):
    def __init__(self):
        print("进入D")
        super().__init__()
        print("离开D")
