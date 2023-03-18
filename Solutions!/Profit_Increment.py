# cook your dish here

for i in range(int(input())):
    x,y=map(int,input().split())
# x is the selling price
# y is the profit earning
    a=x-y
    b=x+(x//10)
    print(b-a)

