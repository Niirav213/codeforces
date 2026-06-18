import sys

def solve():
    n,x = map(int, sys.stdin.readline().split())

    s = 0
    for i in range(3):
        a = list(map(int, sys.stdin.readline().strip().split()))
        for j in range(n):
            if a[j] | x != x:
                break
            s |= a[j]
    if s != x:
        print("NO")
    else:
        print("YES")

if __name__=="__main__":
    l = int(sys.stdin.readline().strip())
    for _ in range(l):
        solve()
