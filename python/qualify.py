# cook your dish here
t=int(input())
for i in range(t):
    tot,esy,hrd=map(int,input().split())
    val=(esy*1)+(hrd*2)
    if(val>=tot):
        print("Qualify")
    else:
        print("NotQualify")