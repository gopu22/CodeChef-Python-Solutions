# cook your dish here

t = int(input())
for i in range(t):
    a,b=map(int, input().split())
    if (100-a)<(200-(b*2)):
        print("FIRST")
    elif (100-a)==(200-(b*2)):
        print("BOTH")
    else:
        print("SECOND")

