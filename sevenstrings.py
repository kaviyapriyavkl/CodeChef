# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    z=x*y
    if(len(str(z))==5 and z!=0):
        print("YES")
    else:
        print("NO")