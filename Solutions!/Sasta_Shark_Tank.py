# cook your dish here

for i in range(int(input())):
    a,b=map(int, input().split())
    if (a*10)>(b*5):
        print("FIRST")
    elif (a*10)==(b*5):
        print("ANY")
    else:
        print("SECOND")

