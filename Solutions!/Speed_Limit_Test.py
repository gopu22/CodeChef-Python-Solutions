# cook your dish here

for i in range(int(input())):
    a,x,b,y=map(int,input().split())
    i=a/x
    j=b/y
    if i>j:
        print("Alice")
    elif i==j:
        print("Equal")
    else:
        print("Bob")

