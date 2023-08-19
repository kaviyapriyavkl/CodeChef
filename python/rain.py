# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    if(n<3):
        print("LIGHT")
    elif(n>=3 and n<7):
        print("MODERATE")
    else:
        print("HEAVY")