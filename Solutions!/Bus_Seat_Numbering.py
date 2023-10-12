# cook your dish here

for i in range(int(input())):
    n=int(input())
    if n<16:
        if n<11:
            print("Lower Double")
        else:
            print("Lower Single")
    else:
        if n<26:
            print("Upper Double")
        else:
            print("Upper Single")

#output

