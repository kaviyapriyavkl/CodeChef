# cook your dish here
t=int(input())
for i in range(t):
    n,m,k=map(int,input().split())
    if(m*k>=n):
        print("YES")
    else:
        print("NO")