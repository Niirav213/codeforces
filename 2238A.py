import sys


def solve():
    n,c = map(int, sys.stdin.readline().split())

    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))

    min_time = 0
    perm_needed = False
    
    for i in range(n):
        if a[i] < b[i]:
            perm_needed = True
            break
    if perm_needed == True:
        a.sort()
        b.sort()
        min_time = c

    for i in range(n):
        if a[i] < b[i]:
            print("-1")
            return
        else:
            sub = a[i] - b[i]
            min_time += sub
    print(min_time)
    return


if __name__=="__main__":
    l = int(sys.stdin.readline())
    for _ in range(l):
        solve()

