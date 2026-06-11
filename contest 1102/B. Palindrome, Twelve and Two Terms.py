import sys


def solve():
    n = int(sys.stdin.readline())

    if n == 10:
        print(-1)
    
    elif n%12 == 10:
        print(22, n-22)

    else:
        print(n % 12, n - (n%12))

if __name__=="__main__":
    l = int(sys.stdin.readline())

    if l:
        for _ in range(l):
            solve()