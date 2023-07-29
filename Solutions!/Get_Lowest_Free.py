# cook your dish here

for i in range(int(input())):
    a,b,c=map(int,input().split())
    x=a,b,c
    print((a+b+c)-min(x))

