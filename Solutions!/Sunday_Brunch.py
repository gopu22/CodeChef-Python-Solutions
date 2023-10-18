# cook your dish here

for _ in range(int(input())):
    x,y=map(int,input().split())
    if (x//y)<=20:
        print(x//y)
    else:
        print(20)

