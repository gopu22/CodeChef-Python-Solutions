# cook your dish here

for i in range(int(input())):
    n,m=map(int,input().split())
    if n-m<=0:
        print(n)
    else:
        print(n-m+n)

