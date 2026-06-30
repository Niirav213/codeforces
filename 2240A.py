import sys

def solve():
    n,k = map(int,(sys.stdin.readline().split()))

    ans = 0

    curr_val = 1

    while n > 0 and curr_val <= n:
        max_copies = n // curr_val

        t = min(k, max_copies)

        ans += t
        n -= t * curr_val

        curr_val *= 2
    print(ans)

if __name__=="__main__":
    l = int(sys.stdin.readline())

    for _ in range(l):
        solve()