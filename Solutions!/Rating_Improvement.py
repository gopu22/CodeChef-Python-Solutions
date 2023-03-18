# cook your dish here

for i in range(int(input())):
    x,y=map(int,input().split())
    if (y>=x and y<=(200+x)):
        print("yes")
    else:
        print("no")

