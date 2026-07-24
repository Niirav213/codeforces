import sys


def solve():
    n = int(sys.stdin.readline())

    c = list(map(int,sys.stdin.readline().split()))

    max_sum = 1
    c.sort()
    if c[0] != 1:
        print("NO")
        return

    ans = True
    for i in range(1,n):
        if c[i] > max_sum:
            ans = False
            break
        max_sum += c[i]

    if ans:
        print("YES")
    else:
        print("NO")

if __name__=="__main__":
    l = int(sys.stdin.readline())

    for _ in range(l):
        solve()