import sys

def solve():
    s = sys.stdin.readline().strip()

    l = len(s)
    s = int(s)

    y = 10**l + 1

    print(y)

if __name__=="__main__":
    l = int(sys.stdin.readline().strip())

    for _ in range(l):
        solve()