# cook your dish here
t=int(input())
for i in range(t):
    t,x,p=map(int,input().split())
    n=(t-x)*-1
    x1=x*3
    r=x1+n
    if(r>=p):
        print("PASS")
    else:
        print("FAIL")