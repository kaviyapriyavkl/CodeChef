# cook your dish here
t= int(input())
for i in range(t):
    n=int(input())
    s=input()
    m=n//2
    if(s[0:m]==s[m:n]):
        print("YES")
    else:
        print("NO")
