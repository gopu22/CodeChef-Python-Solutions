# cook your dish here

for i in range(int(input())):
    a,b,c=map(int,input().split())
    if (a*b)%c==0:
        print(a*b,c)
    elif (b*c)%a==0:
        print(b*c,a)
    elif (c*a)%b==0:
        print(c*a,b)
    else:
        print(-1)

