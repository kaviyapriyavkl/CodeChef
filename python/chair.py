# cook your dish here
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    if(b>a):
        print(0)
    else:
        print(a-b)