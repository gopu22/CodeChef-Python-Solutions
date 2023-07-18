# cook your dish here

for i in range(int(input())):
    a,b,x,y=map(int,input().split())
    if a/x<b/y:
        print("chef")
    elif a/x>b/y:
        print("chefina")
    else:
        print("Both")

