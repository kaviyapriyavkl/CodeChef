# cook your dish here
t=int(input())
for i in range(t):
    c=0
    tot,mon=map(int,input().split())
    lst=list(map(int,input().split()))
    for i in lst:
        if(mon>=i):
            print("1",end="")
            mon-=i
        else:
            print("0",end="")
        c+=1
    if(c==len(lst)):
        print("")
