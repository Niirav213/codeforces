import sys



def solve():
    n = int(sys.stdin.readline().strip())
    ans = []
    

    k = 1 << ((n - 1).bit_length() - 1)

    for i in range(k-1, 0, -1):
        ans.append(i)
    ans.append(0)

    for i in range(k, n):
        ans.append(i)

    print(*ans)


if __name__=="__main__":
    l = int(sys.stdin.readline())

    for _ in range(l):
        solve()