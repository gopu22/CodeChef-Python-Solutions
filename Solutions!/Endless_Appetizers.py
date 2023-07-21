# cook your dish here

for i in range(int(input())):
    x,y,z=map(int,input().split())
    a=z//30
    b=x+a
    if b%y==0:
        print(b//y)
    else:
        print((b//y)+1)

