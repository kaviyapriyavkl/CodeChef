# cook your dish here
t=int(input())
for i in range(t):
    f,t,cr=map(int,input().split())
    tot=(f*5)+(t*10)
    final=tot//cr
    print(final)