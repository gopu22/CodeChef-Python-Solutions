# cook your dish here

for i in range(int(input())):
    n,x=map(int,input().split())
    if n*x>=10000 and n*x<=99999:
        print("Yes")
    else:
        print("No")

