# cook your dish here

t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l2=[]
    count=0
    for j in l:
        for k in l:
            if j!=k and j<k:
                count+=1
        l2.append(count)
        count=0
    print(*l2)

