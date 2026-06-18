import sys


def solve():
    n,k,a,b = map(int,(sys.stdin.readline().split()))
    x = [0] * (n+1)
    y = [0] * (n+1)

    for i in range(1,n+1):
        x[i],y[i] = map(int,(sys.stdin.readline().split()))
        
    ans = abs(x[a] - x[b]) + abs(y[a] - y[b])

    mins = float('inf')
    mint = float('inf')

    for i in range(1, k+1):
        mins = min(mins, abs(x[a]- x[i])+abs(y[a] - y[i]))
        mint = min(mint, abs(x[b]- x[i])+abs(y[b] - y[i]))
    ans = min(ans, mins+mint)

    print(ans)

if __name__=="__main__":
    l = int(sys.stdin.readline())
    for _ in range(l):
        solve()