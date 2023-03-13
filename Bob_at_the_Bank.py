# cook your dish here

for i in range(int(input())):
    w,x,y,z=map(int,input().split())
    a=x*z
    b=y*z
    print(w+a-b)

