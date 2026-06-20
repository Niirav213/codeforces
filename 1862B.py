import sys


def solve():
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))
    ans = []
    for i in range(n):
        if i > 0 and ans[-1] > a[i]:
           ans.append(1) 
        ans.append(a[i])
    print(len(ans))
    print(*ans)


if __name__=="__main__":
    l = int(sys.stdin.readline())
    for _ in range(l):
        solve()