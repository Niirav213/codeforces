import sys

def solve():
    n,s = map(int, sys.stdin.readline().split())

    a = list(map(int, sys.stdin.readline().split()))

    len = -1

    mp = {0: -1}

    sum = 0

    for i in range(n):
        sum += a[i]

        if sum - s in mp:
            len = max(len , i - mp[sum-s])

        if sum not in mp:
            mp[sum] = i

    if len == -1:
        print("-1")
    else:
        print(n - len)

if __name__=="__main__":
    l = int(sys.stdin.readline())

    for _ in range(l):
        solve()