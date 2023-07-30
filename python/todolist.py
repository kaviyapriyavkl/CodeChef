# cook your dish here
T=int(input())

for i in range(T):
    N=int(input())
    d=list(map(int,input().split()))
    count=0
    for j in range(N):
       if(d[j]>=1000):
         count+=1
         continue
    print(count)
        