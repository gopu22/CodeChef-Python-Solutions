# cook your dish here

for i in range(int(input())):
    x,y,z=map(int,input().split())
    a=400/x
    b=400/y
    c=400/z
    if a>b and a>c:
        print("ALICE")
    elif b>a and b>c:
        print("BOB")
    else:
        print("CHARLIE")

