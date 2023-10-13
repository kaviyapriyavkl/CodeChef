# cook your dish here
class Codechef:
    def main(args):
        t = int(input())
        while t > 0:
            n,m=map(int,input().split())
            s = input()
            k = input()
            min_val = float('inf')
            for i in range(n - m + 1):
                count = 0
                sub = s[i:i + m]
                for j in range(m):
                    c1 = sub[j]
                    c2 = k[j]
                    val = abs(ord(c1) - ord(c2))
                    count += min(val, 10 - val)
                if count < min_val:
                    min_val = count
            print(min_val)
            t -= 1

Codechef.main([])