# cook your dish here
t=int(input())
for i in range(t):
    j,T=map(int,input().split())
    if(T>j):
        print("YES")
    else:
        print("NO")