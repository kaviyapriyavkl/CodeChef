# cook your dish here
t=int(input())

for i in range(t):
    a,b,c,d=map(int,input().split())
    if(a+b>=d or b+c>=d or a+c>=d or a>=d or b>=d or c>=d):
        print("YES")
    else:
        print("NO")
