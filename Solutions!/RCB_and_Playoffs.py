# cook your dish here

for i in range(int(input())):
    x,y,z=map(int,input().split())
    a=x+(z*2)
    if a>=y:
        print("Yes")
    else:
        print("No")

