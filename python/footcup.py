# cook your dish here
t=int(input())
for i in range (t):
    a,b=map(int,input().split())
    if(a==b and (a and b!=0)):
        
        print("YES")
    else:
        print("NO")