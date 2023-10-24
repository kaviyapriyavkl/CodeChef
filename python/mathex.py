# cook your dish here
t=int(input())
for i in range(t):
 a,b=map(int,input().split())
 if(a>b or a==b):
    print(0)
 else:
    print(abs(a-b))