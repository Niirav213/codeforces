import sys

def solve():

    n = int(sys.stdin.readline().strip())

    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    c = list(map(int, sys.stdin.readline().split()))

    dp = [-1] * 8
    dp[0] = 0

    for i in range(n):
        next_dp = list(dp)

        for mask in range(8):
            if dp[mask] == -1:
                continue
            if not mask & 1:
                next_dp[mask | 1] = max(next_dp[mask | 1],dp[mask] + a[i])
            if not mask & 2:
                next_dp[mask | 2] = max(next_dp[mask | 2], dp[mask] + b[i])
            
            if not mask & 4:
                next_dp[mask | 4] = max(next_dp[mask | 4], dp[mask] + c[i])
        dp = next_dp
    print(dp[7])

if __name__=="__main__":
    l = int(sys.stdin.readline().strip())
    for _ in range(l):
        solve()