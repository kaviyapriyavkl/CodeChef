# cook your dish here
t=int(input())
for i in range(t):
    a,b,c,d=map(int,input().split())
    if(a+(c*d)==b):
        print("filled")
    elif(a+(c*d)<b):
        print("UnFilled")
    else:
        print("overFlow")