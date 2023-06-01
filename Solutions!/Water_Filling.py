# cook your dish here

for i in range(int(input())):
    a,b,c=map(int,input().split())
    k=a+b+c
    if k>=2:
        print("Not Now")
    else:
        print("Water Filling Time")

