# cook your dish here
t=int(input())
for i in range(t):
     l,k=map(int,input().split())
     if((l*15)>=k*2):
         print("yes")
     else:
         print("NO")
