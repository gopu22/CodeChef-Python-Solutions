# cook your dish here

for i in range(int(input())):
    n,k=map(int,input().split())
    h=list(map(int,input().split()))
    c=0
    for j in h:
        if(j>k):
            c=c+1
    print(c)

