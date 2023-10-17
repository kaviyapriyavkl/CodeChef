# cook your dish here
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    t1=(500-(a*2))+(1000-((b+a)*4))
    t2=(1000-(b*4))+(500-((b+a)*2))
    print(max(t1,t2))
    # print(500-(a*2))
    # print(1000-(a*4))
    
