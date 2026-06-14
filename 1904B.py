import sys
from bisect import bisect_left


def solve():
    n = int(sys.stdin.readline())

    a = list(map(int, sys.stdin.readline().split()))


    v = []

    for i in range(n):
        v.append((a[i], i))

    v.sort()
    pre = [0] * n
    pre[0] = v[0][0]
    for i in range(1,n):
        pre[i] += pre[i-1] + v[i][0]
    
    ans = [0] * n
    for i in range(n):
        j = i
        found= i
        while j<n:
            temp = (pre[j] + 1, -float('inf'))
            idx = bisect_left(v,temp)
            idx -= 1
            if idx == j:
                break
            found += idx -j
            j = idx
        ans[v[i][1]] = found
    print(*ans)


if __name__=="__main__":
    l = int(sys.stdin.readline())
    for _ in range(l):
        solve()
