# cook your dish here

for _ in range(int(input())):
    x,y,z=map(int,input().split())
    assignment_time=x*y
    completion_time=z*24*60
    if assignment_time<=completion_time:
        print('Yes')
    else:
        print('No')

