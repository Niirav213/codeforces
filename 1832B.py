import sys

def solve():
    n, k = map(int, sys.stdin.readline().split())

    a = list(map(int, sys.stdin.readline().strip().split()))

    a.sort()

    for _ in range(k):
        if a[0] + a[1] > a[n-1]:
            del a[n-1]
            n = n-1
        else:
            del a[0:2]
            n = n-2
    print(sum(a))

if __name__=="__main__":
    l = int(sys.stdin.readline().strip())

    for _ in range(l):
        solve()
        