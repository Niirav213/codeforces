import sys

def solve():
    n,c = map(int,(sys.stdin.readline().split()))

    a = list(map(int,(sys.stdin.readline().split())))

    cost = [(a[i] + (i+1)) for i in range(n)]
    cost.sort()
    ans = 0
    i = 0
    while i < n and cost[i] <= c:
        c -= cost[i]
        ans += 1
        i += 1
    print(ans)


if __name__=="__main__":
    l = int(sys.stdin.readline())
    for _ in range(l):
        solve()