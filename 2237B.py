import bisect
import sys

def solve():
    n = int(sys.stdin.readline())
    a = list(map(int , sys.stdin.readline().split()))
    b = list(map(int , sys.stdin.readline().split()))

    is_valid = True
    ans = 0
    c = [0] * n

    for i in range(n):
        idx = bisect.bisect_left(b, a[i])
        if idx == len(b):
            is_valid = False
            break
        c[i] = b[idx]
        b.pop(idx)
    
    if not is_valid:
        print(-1)
        return
    
    
    for i in range(n):
            for j in range(i+1,n):
                if c[i] > c[j]:
                    ans += 1
    
    print(ans)


if __name__=="__main__":
    l = int(sys.stdin.readline().strip())
    for _ in range(l):
        solve()