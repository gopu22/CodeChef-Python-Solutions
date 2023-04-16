# cook your dish here

for i in range(int(input())):
    Pa,Pb,Qa,Qb=map(int,input().split())
    if (max(Pa,Pb)) < (max(Qa,Qb)):
        print("P")
    elif (max(Pa,Pb)) > (max(Qa,Qb)):
        print("Q")
    else:
        print("TIE")

