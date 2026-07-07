import sys

def solve():
    n = int(sys.stdin.readline().strip())

    a = list(map(int, sys.stdin.readline().split()))

    for i in range(57):
        power = 2**i

        is_bin = set()

        for j in range(n):
            is_bin.add(a[j] % power)
        if len(is_bin) == 2:
            print(power)
            return

if __name__=="__main__":
    l = int(sys.stdin.readline())

    for _ in range(l):
        solve()
