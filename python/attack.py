
# cook your dish here
t=int(input())
for i in range(t):
    h,x,y=map(int,input().split())
    a=h-y
    if(a%x==0):
        print((a//x)+1)
    else:
        print((a//x)+2)
