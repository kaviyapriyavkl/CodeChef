test=int(input())
while(test!=0):
    length=int(input())
    index=list(map(int,input().split()))
    if(length%2)!=0:
        print('-1')
    elif(sum(index))==0:
        print(0)
    else:
        if((sum(index))<=0):
            print((sum(index)//2)*-1)
        else:
            print(sum(index)//2)
    test-=1
        
    