# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if(x<y):
        z=y-x
        print(z)
    else:
        z=x-y
        print(z)