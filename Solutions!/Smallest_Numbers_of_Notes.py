# cook your dish here

for _ in range(int(input())):
    N = int(input())
    c = 0
    for x in [100,50,10,5,2,1]:
        c += N//x
        N %= x
    print(c)

