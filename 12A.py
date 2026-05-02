import sys

def solve():
    grid = [sys.stdin.readline().strip() for _ in range(3)]

    s = ''.join(grid)

    if s == s[::-1]:
        print("YES")
        return
    else:
        print("NO")
        return

solve()