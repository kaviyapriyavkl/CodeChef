# cook your dish here
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    count=0
    if(n<=x):
        print("0")
    else:
        while(x<n):
            x=x+4
            count+=1
            if(x>=n):
                break
        print(count)

