import sys

def solve():
    n, k = map(int, sys.stdin.readline().split())

    a = list(map(int, sys.stdin.readline().strip().split()))

    a.sort()
    pr = [0]*(n+1)
    ans = 0
    for i in range(n):
        pr[i+1] = pr[i] + a[i]
    
    for i in range(k+1):
        ans = max(ans, pr[n - (k  - i)] - pr[2 * i])
    print(ans)


if __name__=="__main__":
    l = int(sys.stdin.readline().strip())

    for _ in range(l):
        solve()
        