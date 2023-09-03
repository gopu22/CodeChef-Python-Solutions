# cook your dish here

for i in range(int(input())):
    x,y=map(int,input().split())
    m=(x+y)//2
    chef=abs(m-x)
    chefina=abs(m-y)
    print(max(chef,chefina))

