import sys

def solve():
    n,x = map(int, sys.stdin.readline().split())

    a = list(map(int, sys.stdin.readline().split()))

    an = a[n-1]

    max_dist = a[0]

    for i in range(1,n):
        max_dist = max(max_dist, abs(a[i] - a[i-1]))
    
    min_vol = max(max_dist, 2*(x - an))
    print(min_vol)


def main():
    t = int(sys.stdin.readline())
    if t:
        for _ in range(t):
            solve()


if __name__=="__main__":
    main()