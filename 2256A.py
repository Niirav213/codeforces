import sys


def solve():
    a = list(map(int, sys.stdin.readline().split()))

    a.sort()

    while a[0] + a[1] < a[2]:
        a[2] = a[0] + a[1]
        a.sort()

    print(a[2] - a[0])

if __name__=="__main__":
    l = int(sys.stdin.readline())
    for _ in range(l):
        solve()
    