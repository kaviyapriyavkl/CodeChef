# cook your dish here
for i in range(int(input())):
        a=int(input())
        b=a/100
        c=b*20
        if 100%c==0:
                print(int(100//c))
        else:
                print(int((100//c)+1))