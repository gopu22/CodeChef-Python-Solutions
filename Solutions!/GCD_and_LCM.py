# cook your dish here

import math
for i in range(int(input())):
    a,b=map(int,input().split())
    GCD=math.gcd(a,b)
    LCM=math.lcm(a,b)
    print(GCD, LCM)

