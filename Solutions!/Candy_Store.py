# cook your dish here

for i in range(int(input())):
  X,Y = map(int,input().split())
  if Y <= X:
    print(Y)
  else:
    print(X+((Y-X)*2))

