# cook your dish here

for i in range(int(input())):
    n,x=map(int,input().split())
    l=list(map(int,input().split()))
    sum=0
    for i in range(len(l)):
        sum=sum+l[i]
    c=(x*n)-sum
    if c>=0:
        print(c)
    else:
        print(0)

