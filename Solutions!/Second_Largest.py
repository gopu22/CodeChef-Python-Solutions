# cook your dish here

for i in range(int(input())):
    nums=list(map(int,input().split()))
    nums.remove(max(nums))
    print(max(nums))


#--------------------------------------- OR -------------------------------------------



# cook your dish here

for i in range(int(input())):
    nums=list(map(int,input().split()))
    x=sorted(nums)
    print(x[1])




