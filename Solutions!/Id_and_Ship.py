# cook your dish here

T=int(input())
for _ in range(T):
    t=input()
    if t=='B' or t=='b':
        print("BattleShip")
    elif t=='C' or t=='c':
        print("Cruiser")
    elif t=='D' or t=='d':
        print("Destroyer")
    else:
        print("Frigate")

