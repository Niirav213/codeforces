import sys

def solve():
    n,r,b = map(int, sys.stdin.readline().split())

    p = r // (b+1)
    q = r % (b+1)
    y = ''

    for i in range(p):
        y = y + 'R'
    ans = ""

    for i in range(b+1):
        if i > 0:
            ans = ans + 'B' 
        ans = ans + y

        if q > 0:
            ans = ans + 'R'
        q -= 1
    print(ans)


if __name__=="__main__":
    l = int(sys.stdin.readline().strip())

    for _ in range(l):
        solve()
