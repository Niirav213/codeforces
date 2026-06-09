import sys

def solve():
    n,k,b,s = map(int, sys.stdin.readline().split())

    min_s = k * b
    max_s = k * b + (k-1)*n

    if s < min_s or s > max_s:
        print(-1)
    
    else:
        ans = [0] * n
        ans[0] = k * b
        s -= min_s

        for i in range(n):
            add = min(k-1, s)
            ans[i] += add
            s -= add

        print(*ans)
    
if __name__=="__main__":
    l = int(sys.stdin.readline())
    if l:
        for _ in range(l):
            solve()