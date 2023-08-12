# cook your dish here

for i in range(int(input())):
    a,b,c=map(int,input().split())
    x=a*b
    y=a+c
    print(min(x,y))

