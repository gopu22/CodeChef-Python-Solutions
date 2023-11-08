# cook your dish here

for i in range(int(input())):
    x,y=map(int,input().split())
    diff=abs(x-y)
    if x==y:
        print(0)
    elif x<y:
        print(diff)
    else:
        if diff%2==0:
            print(diff//2)
        else:
            print((diff//2)+2)

