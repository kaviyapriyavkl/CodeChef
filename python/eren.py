# cook your dish here
t=int(input())
for i in range(t):
    e=0
    o=0
    a,b,c=map(int,input().split())
    if(a==1):
        print((0*b)+(1*c))
    else:
        for i in range(1,a+1):
            if(i%2==0):
                e+=1
                
            else:
                o+=1
        print((e*b)+(o*c))
