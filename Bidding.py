# cook your dish here

T=int(input())
for i in range(T):
    a,b,c=map(int,input().split())
    hash = {a:'Alice', b:'Bob', c:'Charlie'}
    print(hash[max(a,b,c)])


#---------------------------------------------OR-----------------------------------------------#

# cook your dish here

T=int(input())
for i in range(T):
    a,b,c=map(int,input().split())
    if a>b and a>c:
        print('Alice')
    elif b>a and b>c:
        print('Bob')
    elif c>a and c>b:
        print('Charlie')

