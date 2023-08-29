# cook your dish here
t=int(input())
for i in range(t):
    x=int(input())
    if(x>70 and x<=100):
        print("500")
    elif(x>100):
        print("2000")
    else:
        print("0")