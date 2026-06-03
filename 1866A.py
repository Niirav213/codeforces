import sys

def solve():
    n = int(sys.stdin.readline().strip())

    a = list(map(int, sys.stdin.readline().split()))
    a = [abs(i) for i in a]
    a.sort()
    print(abs(a[0]))

if __name__=="__main__":
    solve()