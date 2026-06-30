import sys


def solve():
    n = int(sys.stdin.readline())

    ans = 0

    for b in range(1,n+1):
        div = n // b

        ans += div**2

    print(ans)


if __name__=="__main__":
    l = int(sys.stdin.readline().strip())
    for _ in range(l):
        solve()