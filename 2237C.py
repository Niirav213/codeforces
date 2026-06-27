import sys

def solve():
    n = int(sys.stdin.readline().strip())
    
    a = list(map(int, sys.stdin.readline().split()))

    m = 0
    for i in range(n):
        if m > a[i]:
            m = m + a[i]
        else:
            m = a[i]
        
    print(m)


if __name__=="__main__":
    l = int(sys.stdin.readline().strip())
    
    for _ in range(l):
        solve()