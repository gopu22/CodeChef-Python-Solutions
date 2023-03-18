# cook your dish here

for i in range(int(input())):
    a,b,c=map(int,input().split())
    if (a+b)%2!=0 or (b+c)%2!=0 or (c+a)%2!=0:
        print("yes")
    else:
        print("no")

