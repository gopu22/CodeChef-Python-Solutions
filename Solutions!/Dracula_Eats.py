# cook your dish here

for _ in range(int(input())):
    n=int(input())
    c=0
    if n<=1:
        print(c)
    else:
        for i in range(2,n+1,7):
            c+=1
        print(c)

