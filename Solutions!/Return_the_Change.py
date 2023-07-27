# cook your dish here

for i in range(int(input())):
    n=int(input())
    nearest=round(n/10)*10
    if abs(n-nearest>=5):
        nearest+=10
    print(100-nearest)

