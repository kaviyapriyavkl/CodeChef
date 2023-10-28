# cook your dish here
t=int(input())
for i in range(t):
    a,b,c,d=map(int,input().split())
    n=0
    if((a==c or a==d) and (b==c or b==d)):
        print(0)
    elif((a==c or a==d) or (b==c or b==d)):
        print(1)
    else:
        print(2)
    
    
    
