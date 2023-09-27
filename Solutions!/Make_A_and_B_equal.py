# cook your dish here

for _ in range(int(input())):
    a,b=list(map(int,input().split()))
    min_,max_=min(a,b),max(a,b)
    if a==b:
        print("yes")
    else:
        while(min_<max_):
            min_=min_*2
        if min_==max_:
            print("yes")
        else:
            print("no")

