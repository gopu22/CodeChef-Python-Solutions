# cook your dish here

for i in range(int(input())):
    x,y=map(int,input().split())
    if x<y:
        print("REPAIR")
    elif x>y:
        print("NEW PHONE")
    else:
        print("ANY")
# final output
