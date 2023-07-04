# cook your dish here

for i in range(int(input())):
    x,y,z=map(int,input().split())
    if (abs(x-y)<=z):
        print("yes")
    else:
        print("no")

