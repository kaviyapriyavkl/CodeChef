# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    x=x*100
    y=y*100
    if((y/x)*100>=50):
        print("YES")
    else:
        print("NO")
    