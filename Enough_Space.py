# cook your dish here

T=int(input())
for i in range(T):
    N,X,Y=map(int,input().split())
    if (N>=(X+Y*2)):
        print('yes')
    else:
        print('no')
 
 #---------------------------------------------OR----------------------------------------------#
 
 # cook your dish here
 
T=int(input())
for i in range(T):
    N,X,Y=map(int,input().split())
    P=X+(Y*2)
    if N>=P:
        print('yes')
    else:
        print('no')

