import sys


def solve():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))

    pre = [0] * n
    pre[0] = a[0]
    for i in range(1,n):
        pre[i] = a[i] + pre[i-1]
    
    ans = 0

    for k in range(1, n):
        if n % k != 0:
            continue

        start = k-1
        maxi = pre[start]
        mini = pre[start]
        for idx in range(start +k, n, k):
            curr = pre[idx] - pre[idx - k]
            maxi = max(maxi, curr)
            mini = min(mini, curr)
        ans = max(ans, maxi - mini)
    print(ans)

if __name__=="__main__":
    l = int(sys.stdin.readline())
    for _ in range(l):
        solve()