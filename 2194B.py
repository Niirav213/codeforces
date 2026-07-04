import sys

def solve():
    n, x, y = map(int, sys.stdin.readline().split())

    a = list(map(int, sys.stdin.readline().split()))


    ans =[0] * n

    sall = 0
    for i in range(n):
        sall += a[i] // x

    max_rubles = 0

    from_other = 0
    curr = 0

    for i in range(n):
        from_other = sall - (a[i] // x)
        curr = a[i] + from_other * y
        if curr > max_rubles:
            max_rubles = curr
    print(max_rubles)

if __name__=="__main__":
    l = int(sys.stdin.readline().strip())

    for _ in range(l):
        solve()
