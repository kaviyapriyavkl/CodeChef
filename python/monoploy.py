# cook your dish here
t=int(input())
for i in range(t):
    lst=list(map(int,input().split()))
    mx=max(lst)
    if(mx>sum(lst)-mx):
        print("YES")
    else:
        print("NO")
    