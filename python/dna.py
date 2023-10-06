# cook your dish here
t=int(input())
for i in range(t):
    num=int(input())
    s=input()
    new =''
    for i in range(0,num):
        if(s[i]=="A"):
            new+="T"
        elif(s[i]=="T"):
            new+="A"
        elif(s[i]=="C"):
            new+="G"
        elif(s[i]=="G"):
            new+="C"
    print(new)
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    