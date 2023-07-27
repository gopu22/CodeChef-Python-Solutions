# cook your dish here

for i in range(int(input())):
    n=int(input())
    output=1
    for j in range(1,n+1):
        output=output*j
        j-=1
    print(output)

