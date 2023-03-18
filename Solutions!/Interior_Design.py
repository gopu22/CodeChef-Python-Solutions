# cook your dish here

T=int(input())
for i in range(T):
    x1, y1, x2, y2=map(int,input().split())
    if (x1+y1<x2+y2):
        print(x1+y1)
    else:
        print(x2+y2)

#--------------------------------------------------OR----------------------------------------------------

# cook your dish here
T=int(input())
for i in range(T):
    x1, y1, x2, y2=map(int,input().split())
    print(min(x1+y1, x2+y2))

