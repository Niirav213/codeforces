import sys

def solve():
    n,m = map(int,(sys.stdin.readline().split()))

    a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    columns = list(zip(*a))

    total_ans = 0

    for col in columns:
        sorted_col = sorted(col)

        pref_sum = 0

        for i,val in enumerate(sorted_col):
            total_ans += val * i - pref_sum
            pref_sum += val
    print(total_ans)


if __name__=="__main__":
    l = int(sys.stdin.readline())

    for _ in range(l):
        solve()
