h=int(input())
for i in range(h):
    x,y,z=map(int,input().split())
    if(x<=y): #demand less than the one jar capacity
       print(z)
    elif(x>y): #demand greater than the one jar capacity
        if(x%y==0):
            print((x//y)*z)
        else:
            print((x//y)*z+z)