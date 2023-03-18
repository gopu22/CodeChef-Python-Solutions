# cook your dish here

T=int(input())
for i in range(T):
    x,y=map(int,input().split())
    a=x*3
    b=y*2
    if a>b:
        print(b)
    else:
        print(a)

