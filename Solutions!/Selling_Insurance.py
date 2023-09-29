# cook your dish here

for _ in range(int(input())):
    x=int(input())
    ans=x*0.2
    if 100%ans==0:
        print(int(100//ans))
    else:
        print(int(100//ans)+1)

