# cook your dish here
t=int(input())
for i in range(t):
    Pa,Pb,Qa,Qb =map(int,input().split())
    p=max(Pa,Pb)
    q=max(Qa,Qb)
   
    if(q>p):
        print("P")
    elif(p>q):
        print("Q")
    else:
        print("TIE")
    
    