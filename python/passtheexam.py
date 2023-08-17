# cook your dish here
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    x=a+b+c
    if(x>=100 and a>=10 and b>=10 and c>=10):
        print("PASS")
    else:
        print("FAIL")
    