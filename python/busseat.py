# cook your dish here
t=int(input())
for i in range (t):
    n=int(input())
    if(n in range(1,11)):
        print("Lower Double")
    elif(n in range(11,16)):
        print("Lower Single")
    elif(n in range(16,26)):
        print("Upper Double")
    elif(n in range(26,31)):
        print("Upper Single")
    
    