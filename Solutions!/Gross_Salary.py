# cook your dish here

for i in range(int(input())):
    t=int(input())
    if t>=1500:
        hra=500
        da=0.98*t
    else:
        hra=0.1*t
        da=0.9*t
    print(t+hra+da)

