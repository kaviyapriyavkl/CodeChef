t=int(input())
for i in range(t):
    a=list(map(int,input().split()))
    if(sum(a)==180):
        print("YES")
    else:
        print("NO")