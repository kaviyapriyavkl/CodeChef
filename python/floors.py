# cook your dish here
t = int(input())
for i in range(t) :
    a,b = map(int,input().split())
    for n in range(0,11) :
        if (n*10)>=a :
            c = n 
            break 
    for n in range(0,11) :      
        if (n*10)>=b :
            d = n 
            break 
    print(abs(c-d))