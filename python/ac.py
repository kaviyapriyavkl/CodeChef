# cook your dish here
t = int(input())

for i in range(t):
    a,b,c=map(int,input().split())
    min=0
    if a>c:
        min=a
    else:
        min=c
                
    if min<=b:
        print("YES")
    else:
        print("NO")
        
