import sys


def solve():
    n = int(sys.stdin.readline())

    b1 = list(range(1, n+1))

    
    b2 = list(range(n, 0, -1))

    rev = list(range(n, 0, -1))

    b3 = rev[2:] + rev[:2]  

    b4  = list(range(2, n+1)) + [1]

    ans = b1 + b2 + b3 + b4
    print(*ans)

if __name__=="__main__":
    l = int(sys.stdin.readline())
    if l:
        for _ in range(l):
            solve()