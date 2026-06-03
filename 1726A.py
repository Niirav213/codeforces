import sys

def solve():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))

    ans=max(a[-1]-min(a),max(a)-a[0])
    for i in range(n):
        ans=max(ans,a[i-1]-a[i])
    print(ans)

def main():
    l = int(sys.stdin.readline())
    if l:
        for _ in range(l):
            solve()

if __name__=="__main__":
    main()