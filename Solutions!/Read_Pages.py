# cook your dish here

for i in range(int(input())):
    n,x,y=map(int,input().split())
    if n<=(x*y):
        print("yes")
    else:
        print("no")

