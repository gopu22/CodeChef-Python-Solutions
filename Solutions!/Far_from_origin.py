# cook your dish here

t = int(input())
for i in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    
    # Calculate distances of Alex and Bob
    dist1 = (x1**2 + y1**2)**0.5
    dist2 = (x2**2 + y2**2)**0.5
    
    # Compare distances and print the result
    if dist1 > dist2:
        print("ALEX")
    elif dist2 > dist1:
        print("BOB")
    else:
        print("EQUAL")

