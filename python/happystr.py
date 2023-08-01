# cook your dish here
t = int(input())
for i in range(t):
    s=input()
    for i in range(len(s)-2):
        if((s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o'or s[i]=='u')and (s[i+1]=='a' or s[i+1]=='e' or s[i+1]=='i' or s[i+1]=='o' or s[i+1]=='u' )and (s[i+2]=='a' or s[i+2]=='e' or s[i+2]=='i' or s[i+2]=='o' or s[i+2]=='u' ) ):
            print("Happy")
            break
    else:
            print("Sad")
        