import sys


def solve():
    n = int(sys.stdin.readline())
    bin_t = sys.stdin.readline().strip()

    removed = [0] * (n+1)
    ans = 0

    for i in range(1, n+1):
        for j in range(i,n+1,i):
            if bin_t[j-1] == '1':
                break

            if removed[j] == 0:
                removed[j] = 1
                ans += i

    
    print(ans)



if __name__=="__main__":
    l = int(sys.stdin.readline().strip())

    for _ in range(l):
        solve()