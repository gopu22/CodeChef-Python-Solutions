# cook your dish here

for i in range(int(input())):
    x,y,z=map(int,input().split())
    if y<=x*10:
        print(y*z)
    else:
        print((x*10)*z)

