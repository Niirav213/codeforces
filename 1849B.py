import sys


def solve():
    n, k = map(int, sys.stdin.readline().split())

    a = list(map(int, sys.stdin.readline().split()))
    health = []
    for i in range(n):
        health.append((a[i], i + 1))

    health = [((x[0] - 1)%k + 1, x[1]) for x in health]

    health = [((x[0] - 1) % k + 1, x[1]) for x in health]
 
    health.sort(key=lambda x: (-x[0], x[1]))

    ans = [str(i[1]) for i in health]
    print(*ans)

def main():
    l = int(sys.stdin.readline())
    if l:
        for _ in range(l):
            solve()

if __name__=="__main__":
    main()