# cook your dish here

for i in range(int(input())):
    n,x=map(int,input().split())
    count=0
    l=list(map(int,input().split()))
    for i in range(n):
        if l[i]>=x:
            count+=1
    print(count)

