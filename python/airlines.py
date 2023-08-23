# cook your dish here
t=int(input())
for i in range(t):
    s,w,r=map(int,input().split())
    tot=s*10
    if(tot<w):
        
        print(tot*r)
    else:
        print(w*r)
    