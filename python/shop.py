# cook your dish here
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    if(a-a*0.1<b):
        print("ONLINE")
    elif(a-a*0.1==b):
        print("EITHER")
    else:
        print("DINING")
        