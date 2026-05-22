import sys

def solve():
    n = int(sys.stdin.readline())
    p = list(map(int, sys.stdin.readline().split()))

    j =0
    for i in range(n):
        if p[i] == n:
            j = i

    temp = p[j]
    p[j] = p[0]
    p[0] = temp

    print(*p)

def main():
    l = int(sys.stdin.readline())

    for _ in range(l):
        solve()

if __name__=="__main__":
    main()

