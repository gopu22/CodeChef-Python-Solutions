# cook your dish here

for i in range(int(input())):
    x,y=map(int,input().split())
    if x<(2*y):
        print(0)
    else:
        print(x//(2*y))

