# cook your dish here

n=int(input())
y=list(map(int, input().split()))
sto=[y[0],y[1],y[2]]
for i in range(3,n):
    x=min(sto[i-1],sto[i-2],sto[i-3])+y[i]
    sto.append(x)
if n<3:
    a=min(y)
else:
    a=min(sto[n-1],sto[n-2],sto[n-3])
print(sum(y)-a)

