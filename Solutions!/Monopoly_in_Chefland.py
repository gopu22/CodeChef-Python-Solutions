# cook your dish here

for i in range(int(input())):
    r1,r2,r3=map(int,input().split())
    if r1>r2+r3 or r2>r1+r3 or r3>r1+r2:
        print("yes")
    else:
        print("no")

