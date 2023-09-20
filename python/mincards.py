# cook your dish here
n=int(input())
for i in range(1,n+1):
    a=int(input())
    if a<=4:
        print(1,end='\n')
    elif a%4==0:
        print(a//4,end='\n')
    else:
        print((a//4)+1,end='\n')