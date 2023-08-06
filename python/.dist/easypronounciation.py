# cook your dish here
t= int(input())
for i in range(t):
    n=int(input())
    s=input()
    v=['a','e','i','o','u']
    for i in range(len(s)-3):
        if(s[i] not in v):
            if(s[i+1] not in v):
                if(s[i+2] not in v):
                    if(s[i+3] not in v):
                        print("NO")
                        break
        else:
            print("YES")