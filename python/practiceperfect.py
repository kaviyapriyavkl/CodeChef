# cook your dish here

count=0
z=list(map(int,input().split()))
for i in z:
    if i>=10:
        count+=1
print(count)