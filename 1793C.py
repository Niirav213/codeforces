import sys

def solve():

    n = int(sys.stdin.readline().strip())
    a = list(map(int,sys.stdin.readline().split()))

    a_set = set(range(1, n+1))


    l = 0
    r = n-1
    low , high = 1, n
    while l <= r:
        if a[l] == low or a[l] == high:
            if a[l] == low:
                low += 1
            else:
                high -= 1
            
            l += 1
            continue
        if a[r] == low or a[r] == high:
            if a[r] == low:
                low += 1
            else:
                high -= 1
            r -= 1
            continue

        break

    if l < r:
        print(l+1, r+1)
    else:
        print(-1)


if __name__=="__main__":
    l = int(sys.stdin.readline())
    for _ in range(l):
        solve()
        

