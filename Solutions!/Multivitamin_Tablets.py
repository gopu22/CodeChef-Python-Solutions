# cook your dish here

T=int(input())
for i in range(T):
    x,y=map(int,input().split())
    print("yes"if y>=x*3 else "no")

