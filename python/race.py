# cook your dish here
t=int(input())
for i in range(t):
    a,b,c,d=map(int,input().split())
    if(a/c>b/d):
        print("Chefina")
    elif(a/c==b/d):
        print("Both")
    else:
        print("Chef")
        