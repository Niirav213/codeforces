import sys


def solve():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))

    mx = 0

    for i in range(n-1):
        mx = max(mx, a[i]-a[i+1])
    
    for i in range(1,n):
        if a[i] < a[i-1]:
            a[i] += mx
    
    if a == sorted(a):
        print("YES")
    else:
        print("NO")


if __name__=="__main__":
    l = int(sys.stdin.readline())
    if l:
        for _ in range(l):
            solve()
            