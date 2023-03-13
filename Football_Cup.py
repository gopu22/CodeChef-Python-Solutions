# cook your dish here

for i in range(int(input())):
    x,y=map(int,input().split())
    if x==0 or y==0 or x!=y:
        print("no")
    else:
        print("yes")

