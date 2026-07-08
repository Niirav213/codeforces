import sys


def solve():
    n = int(sys.stdin.readline())
    a = sorted(map(int, sys.stdin.readline().split()))

    j = 0
    ans = []
    for i in range(n-1, 0 , -1):
        ans.append(a[j])
        j += i
    ans.append(a[-1])
    print(*ans)

if __name__=="__main__":
    l = int(sys.stdin.readline().strip())

    for _ in range(l):
        solve()
    