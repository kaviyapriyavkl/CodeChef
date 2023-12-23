
# cook your dish here
for _ in range(int(input())):
    A,B,C=map(int,input().split())
    print(('No','Yes') [A>B+C or B>A+C or C>A+B])