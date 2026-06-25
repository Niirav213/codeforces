import sys

def solve():
    n = int(sys.stdin.readline().strip())

    a = list(map(int, sys.stdin.readline().split()))
    a1 = list(map(int, sys.stdin.readline().split()))
    
    l, r = -1, -1

    for i in range(n):
        if a[i] != a1[i]:
            r = i
            if l == -1:
                l = r
    while r < n-1 and a1[r+1] >= a1[r]:
        r += 1
    
    while l > 0 and a1[l-1] <= a1[l]:
        l -= 1
    print(l+1, r+1)


if __name__=="__main__":
    l = int(sys.stdin.readline().strip())

    for _ in range(l):
        solve()