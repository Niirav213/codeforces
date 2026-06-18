import sys

def solve():

    n,q = map(int, sys.stdin.readline().split())

    a = list(map(int, sys.stdin.readline().split()))
    x = list(map(int, sys.stdin.readline().split()))

    min_x = 31
    for i in range(q):
        if x[i] >= min_x:
            continue

        val = 2 ** x[i]

        for j in range(n):
            if a[j] % val ==0:
                a[j] += (val // 2)
        min_x = x[i]
    
    print(*a)

if __name__=="__main__":
    l = int(sys.stdin.readline())
    for _ in range(l):
        solve()
