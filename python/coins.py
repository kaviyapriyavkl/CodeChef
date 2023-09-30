# cook your dish here
t=int(input())
for i in range(t):
    a=int(input())
    if(a%10==0):
        c=(a//10)
        print(c)
    elif(a%10!=0 and a%5==0):
        c=(a//10)+1
        print(c)
    else:
        print("-1")