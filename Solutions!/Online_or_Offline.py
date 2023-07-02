# cook your dish here

for i in range(int(input())):
    n,m=map(int,input().split())
    online=n-(n*0.1)
    if online<m:
        print("ONLINE")
    elif m<online:
        print("DINING")
    else:
        print("EITHER")

