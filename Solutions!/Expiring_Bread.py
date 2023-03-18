# cook your dish here

for i in range(int(input())):
    n,m,k=map(int,input().split())
    if (m*k)>=n:
        print("yes")
    else:
        print("no")

