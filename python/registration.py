t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    if(y-z>=x):
        print("YES")
    else:
        print("NO")
        