# cook your dish here

T=int(input())
for i in range(T):
    n,x,k=map(int,input().split())
    if (n*x<=k):
        print('yes')
    else:
        print("no")

