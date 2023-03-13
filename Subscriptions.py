# cook your dish here

for i in range(int(input())):
    n,x=map(int,input().split())
    a=n//6
    if n<6:
        print(x)
    elif n<15:
        print(a*x)
    else:
        print((a+1)*x)

