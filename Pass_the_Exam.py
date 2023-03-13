# cook your dish here

for i in range(int(input())):
    a,b,c=map(int,input().split())
    x=a+b+c
    if a>=10 and b>=10 and c>=10 and x>=100:
        print('pass')
    else:
        print("fail")

