# cook your dish here

for i in range(int(input())):
    x,y=map(int,input().split())
    if(y>=(x*50/100)):
        print("yes")
    else:
        print("no")

