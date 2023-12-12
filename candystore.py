# cook your dish here
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    if(b<a):
        print(b)
    else:
        print(a+2*(b-a))