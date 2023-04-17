# cook your dish here

for i in range(int(input())):
    n,x=map(int,input().split())
    if n>x:
        print(min(x, n-x))
    else:
        print("0")

