import sys
from bisect import bisect_left, bisect_right

def solve():
    n,q = map(int,sys.stdin.readline().split())

    a = list(map(int,sys.stdin.readline().split()))
    k = list(map(int,sys.stdin.readline().split()))

    pref_sum = [0]*n
    pref_sum[0] = a[0]
    max_step = [0] * n
    max_step[0] = a[0]
    for i in range(1,n):
        pref_sum[i] = a[i] + pref_sum[i-1]
        max_step[i] = max(max_step[i-1], a[i])



    ans = []
    for i in k:
        idx = bisect_right(max_step, i)
        if idx == 0:
            ans.append(0)
        else:
            ans.append(pref_sum[idx - 1])
    print(*ans)

if __name__=="__main__":
    l = int(sys.stdin.readline())
    for _ in range(l):
        solve()
