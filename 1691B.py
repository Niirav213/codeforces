import sys
from collections import defaultdict

def solve():
    n = int(sys.stdin.readline().strip())

    s = list(map(int, sys.stdin.readline().split()))

    freq = defaultdict(int)

    for i in s:
        freq[i] += 1
    
    flag = False

    for count in freq.values():
        if count == 1:
            flag = True
            break

    if flag:
        print(-1)
        return
    
    perm = list(range(1, n+1))

    l,r = 0, 0

    while r<n:
        if s[l] == s[r]:
            r += 1
        else:
            perm[l:r] = perm[l+1:r] + perm[l:l+1]
            l = r

    perm[l:r] = perm[l+1:r] + perm[l:l+1]

    print(*perm)

if __name__=="__main__":
    l = int(sys.stdin.readline())
    if l:
        for _ in range(l):
            solve()

