# cook your dish here
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    if(a*100)<(b*10):
        print("Disposable")
    else:
        print("Cloth")