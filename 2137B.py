import sys

def solve():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))

    ans = []
    for i in a:
        ans.append(n - i + 1)

    print(*ans)

def main():
    line = int(sys.stdin.readline())
    if line:
        for _ in range(line):
            solve()

if __name__=="__main__":
    main()