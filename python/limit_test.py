# cook your dish here
t=int(input())
for i in range(t):
    a,a1,b,b1=map(int,input().split())
    if(a/a1>b/b1):
        print("Alice")
    elif(b/b1>a/a1):
        print("Bob")
    else:
        print("Equal")