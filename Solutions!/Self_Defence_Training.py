# cook your dish here

T=int(input())
for i in range(T):
    n=int(input())
    a=list(map(int,input().split(" ")))
    count=0
    for i in a:
        if i>=10 and i<=60:
            count+=1
    print(count)

