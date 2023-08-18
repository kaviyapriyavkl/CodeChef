# cook your dish here
t=int(input())
for i in range(t):
    n=input()
    x=n[::-1]
    if(n==x):
        print("wins")
    else:
        print("loses")
    