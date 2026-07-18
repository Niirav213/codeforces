import sys


def solve():
    n = int(sys.stdin.readline())

    x = list(map(int, sys.stdin.readline().split()))
    y = list(map(int, sys.stdin.readline().split()))

    dff = [y[i] - x[i] for i in range(n)]
    dff.sort()

    ans = 0

    l,r = 0, n-1

    while l < r:
        if dff[r] + dff[l] >= 0:
            ans += 1
            l += 1
            r -= 1
        else:
            l += 1
    
    print(ans)

if __name__=="__main__":
    l = int(sys.stdin.readline())
    for _ in range(l):
        solve()
    