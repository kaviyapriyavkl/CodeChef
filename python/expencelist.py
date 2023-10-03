# cook your dish here
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    c=(pow(2,b))
    for i in range(0,a):
        d=c-(c//2)
        c=d
    print(d)