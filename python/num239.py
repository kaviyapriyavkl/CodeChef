# cook your dish here
t=int(input())
for i in range(t):
    l,r=map(int,input().split())
    count=0
    for i in range(l,r+1):
        if(i%10==2 or i%10==3 or i%10==9):
            count=count+1
        else:
            continue
    print(count)
            