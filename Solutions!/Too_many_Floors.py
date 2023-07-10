# cook your dish here

import math as m
for i in range(int(input())):
    x,y=map(int,input().split())
    f1=m.ceil(x/10)
    f2=m.ceil(y/10)
    print(abs(f1-f2))

