# cook your dish here
t=int(input())
for i in range(t):
    d=list(map(int,input().split()))
    d.sort()
    print(d[1])
    