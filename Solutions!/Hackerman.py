# cook your dish here

prime = [1,2,3,5,7,11]
for i in range(int(input())):
    a,b=map(int,input().split())
    if a+b in prime:
        print("Alice")
    else:
        print("Bob")

