# cook your dish here
import math as math
t=int(input())
for i in range(t):
    x1,y1,x2,y2=map(int,input().split())
    d1=math.sqrt(((x1-0)**2)+((y1-0)**2))
    d2=math.sqrt(((x2-0)**2)+((y2-0)**2))
    if(d1==d2):
        print("EQUAL")
    elif(d1>d2):
        print("ALEX")
    else:
        print("BOB")