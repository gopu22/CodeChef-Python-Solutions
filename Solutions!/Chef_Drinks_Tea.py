# cook your dish here

for i in range(int(input())):
    x,y,z=map(int,input().split())
    if x<=y:
        print(z)
    elif x>y:
        if x%y==0:
            print((x//y)*z)
        else:
            print((x//y)*z+z)

