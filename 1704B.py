import sys

def solve():
    n,x = map(int, sys.stdin.readline().split())

    a = list(map(int, sys.stdin.readline().split()))
    ans = 0

    segments = [(a[i]-x, a[i]+x) for i in range(n)]
    l,r = segments[0]

    for i in range(1,n):
        l = max(l, segments[i][0])
        r = min(r, segments[i][1])

        if l>r:
            ans += 1
            l,r = segments[i]
    print(ans)

if __name__=="__main__":
    l = int(sys.stdin.readline())
    if l:
        for _ in range(l):
            solve()