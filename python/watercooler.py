# cook your dish here
t=int(input())

for i in range(t):
    x,y,m=map(int,input().split())
    a=x*m
    if(a>=y ):
        print("NO")
    else:
        print("YES")