# cook your dish here

T=int(input())
for i in range(T):
    x,y=map(int,input().split())
    if x<2*y:
        print("no")
    else:
        print("yes")

