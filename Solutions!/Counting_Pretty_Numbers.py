# cook your dish here

for i in range(int(input())):
  L,R = map(int,input().split())
  count = 0
  l = [2,3,9]
  for i in range(L,R+1):
    if i%10 in l:
      count+=1
  print(count)

