import sys

def solve():
    n = int(sys.stdin.readline())

    a = list(map(int, sys.stdin.readline().split()))

    a.sort(reverse=True)

    print((a[0]+1)- a[n-1])

if __name__=="__main__":
    l = int(sys.stdin.readline())
    if l:
        for _ in range(l):
            solve()

