# cook your dish here

for i in range(int(input())):
    n,m=map(int,input().split())
    if n<=(6*6*m):
        print("yes")
    else:
        print("no")

