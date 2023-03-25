# cook your dish here

for i in range(int(input())):
    x,y,z=map(int,input().split())
    if (z%x==0) and (z%y!=0):
        print("Chicken")
    elif (z%y==0) and (z%x!=0):
        print("Duck")
    elif (z%x==0) and (z%y==0):
        print("Any")
    else:
        print("None")

