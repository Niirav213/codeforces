import sys

def solve():
    n,k = map(int, sys.stdin.readline().split())

    a = list(map(int,sys.stdin.readline().split()))
    b = list(map(int,sys.stdin.readline().split()))

    sm, res , mx = 0, 0, 0
    for i in range(min(n,k)):
        sm += a[i]
        mx = max(mx, b[i])
        res = max(res, sm + mx * (k - i - 1))
    
    print(res)

if __name__=="__main__":
    l = int(sys.stdin.readline())
    if l:
        for _ in range(l):
            solve()
