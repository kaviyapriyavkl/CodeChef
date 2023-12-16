# cook your dish here
t=int(input())
for i in range(t):
    a,b,c,d=map(int,input().split())
    if(a-c>b-d):
        print("Second")
    elif(b-d>a-c):
        print("First")
    else:print("any")