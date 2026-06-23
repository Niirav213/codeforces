import sys


def solve():
    n = int(sys.stdin.readline().strip())
    a = list(map(int , sys.stdin.readline().split()))

    a.sort()

    if a[0] == a[n-1]:
        print("-1")
        return
    
    else:
        it = 0
        while a[it] == a[0]:
            it += 1
        b = a[:it]
        c = a[it:]
        
    
    print(len(b), len(c))
    print(*b)
    print(*c)

if __name__=="__main__":
    l = int(sys.stdin.readline())
    for _ in range(l):
        solve()