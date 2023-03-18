# cook your dish here

for i in range(int(input())):
    x,y=map(int,input().split())
    a=(100*x)
    b=(10*y)
    if a<b:
        print('Disposable')
    else:
        print('cloth')

