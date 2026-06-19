import sys

def solve():

    a,b,x = map(int, sys.stdin.readline().strip().split())
    i = 0
    ans = 1e18
    while a != b:
        if b>a:
            temp = a
            a = b
            b = temp
        ans = min(ans, abs(a - b) + i)
        a //= x
        i += 1
    ans = min(ans, i)

    print(ans)

if __name__=="__main__":
    l = int(sys.stdin.readline().strip())
    for _ in range(l):
        solve()
        