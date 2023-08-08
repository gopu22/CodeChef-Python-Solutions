# cook your dish here

for i in range(int(input())):
    a,b,c,d,e,f=list(map(int,input().split()))
    x=(a+b+c)-min(a,b,c)
    y=(d+e+f)-min(d,e,f)
    if x>y:
        print("Alice")
    elif y>x:
        print("Bob")
    else:
        print("Tie")

