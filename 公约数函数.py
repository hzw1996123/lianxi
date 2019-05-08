def gcd(x,y):
    while y:
        t = x % y
        x = y
        y = t
    return x
