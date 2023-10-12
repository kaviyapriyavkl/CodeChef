# cook your dish here
t=int(input())
for i in range(t):
    a=list(map(int,input().split()))
    if(max(a)>sum(a)-max(a)):
        print("YES")
    else:
        print("NO")
    