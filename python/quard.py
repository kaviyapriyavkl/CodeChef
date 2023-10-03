# cook your dish here
t=int(input())
for i in range(t):
    a,b,c,d=map(int,input().split())
    s1=a+c
    s2=b+d
    if(s1==180 and s2==180):
        print("YES")
    else:
        print("NO")