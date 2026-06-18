
import sys

def solve():
    n = int(sys.stdin.readline().strip())

    a = list(map(int,sys.stdin.readline().strip().split()))

    for i in range(n-1):
        if a[i+1] > a[i]:
            a[i+1] = a[i]
    
    print(sum(a))

if __name__=="__main__":
    l = int(sys.stdin.readline().strip())
    for _ in range(l):
        solve()