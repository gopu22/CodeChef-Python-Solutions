# cook your dish here

for i in range(int(input())):
    a,b,x,y=map(int,input().split())
    if (a<=b and b-a<=x) or (a>=b and a-b<=y):
        print("YES")
    else:
        print("NO")

