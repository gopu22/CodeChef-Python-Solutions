# cook your dish here

for i in range(int(input())):
    n,x,k=map(int,input().split())
    a=k//x
    if n>a:
        print(a)
    else:
        print(n)

#----------------------------------------OR-----------------------------------------------

# cook your dish here

for i in range(int(input())):
    n,x,k=map(int,input().split())
    a=k//x
    print(min(n, a))



