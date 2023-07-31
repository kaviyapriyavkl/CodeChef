# cook your dish here
t=int(input())
a=''
for i in range(t):
    x=list(input())
    y=list(input())
    for j in range(0,len(x)):
        if(x[j]==y[j]):
            a+="G"
        else:
            a+="B"
    print(a)
    a=''
    
    
    