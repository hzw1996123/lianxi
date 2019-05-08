from random import random
from time import perf_counter
dates = 10000**2
hits = 0.0
start = perf_counter()
for i in range(1,dates):
    x,y = random(),random()
    dist = pow(x**2 + y**2,0.5)
    if dist <= 1.0:
        hits = hits + 1
pi = 4 * (hits/dates)
print('圆周率：',pi)
print('运行时间是：',(perf_counter() - start))
