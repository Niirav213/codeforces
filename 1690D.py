import sys

def solve():
    n,k = map(int, sys.stdin.readline().split())

    s = sys.stdin.readline().strip()
    wCount = s[:k].count('W')
    ans = wCount
    for i in range(k,n):

        if s[i] == 'W':
            wCount += 1
        if s[i-k] == 'W':
            wCount -= 1
        ans = min(ans, wCount)
    print(ans)
    return

if __name__=="__main__":
    l = int(sys.stdin.readline())
    for _ in range(l):
        solve()