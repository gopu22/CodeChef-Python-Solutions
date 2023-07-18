# cook your dish here

for i in range(int(input())):
    n,x,p=map(int,input().split())
    a=(n-x)*1
    b=(x*3)-a
    if b>=p:
        print("PASS")
    else:
        print("FAIL")

