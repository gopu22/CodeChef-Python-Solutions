# cook your dish here

n = int(input())
N = list(map(int,input().split()))
e =0
o = 0
for i in N:
    if(i%2!=0):
        o+=1 
    else:
        e+=1 
if(o>=e):
    print("NOT READY")
else:
    print("READY FOR BATTLE")

