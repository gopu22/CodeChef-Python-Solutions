# cook your dish here

for _ in range(int(input())):
    h,x,y=map(int,input().split())
    a=h-y
    if (a%x)==0:
        print((a//x)+1)
    else:
        print((a//x)+2)

