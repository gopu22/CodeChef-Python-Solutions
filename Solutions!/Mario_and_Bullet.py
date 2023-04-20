# cook your dish here

for i in range(int(input())):
    x,y,z=map(int,input().split())
    a=y//x
    if (z-a) > 0:
        print(z-a)
    else:
        print(0)

