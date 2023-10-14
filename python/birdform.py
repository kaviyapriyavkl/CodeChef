# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    if(z%x==0 and z%y==0):
        print("any")
    elif(z%x!=0 and z%y==0):
        print("Duck")
    elif(z%x==0 and z%y!=0):
        print("CHICKEN")
    else:
        print("NONE")
        
