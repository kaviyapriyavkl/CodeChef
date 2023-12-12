# cook your dish here
t=int(input())
for i in range(t):
    s,p=map(int,input().split())
    np=(s*1.10)-(s-p)
    print(int(np))