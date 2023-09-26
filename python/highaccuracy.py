# cook your dish here
t=int(input())
for i in range(t):
    a=int(input())
    if(a%3==0):
        print(0)
    else:
        print(3-(a%3))
    