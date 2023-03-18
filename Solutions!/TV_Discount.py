# cook your dish here

T=int(input())
for i in range(T):
    a,b,c,d=map(int,input().split())
    x=a-c
    y=b-d
    if x<y:
        print("first")
    elif x==y:
        print("any")
    else:
        print("second")

