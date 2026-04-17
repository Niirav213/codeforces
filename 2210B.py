import sys

def solve():
    n = int(sys.stdin.readline())
    p = list(map(int, sys.stdin.readline().split()))
    
    ans = 0
    for i in range(n):
        if p[i] <= i + 1:
            ans += 1
    print(ans)

def main():
    line = int(sys.stdin.readline().strip())
    if line:
        for _ in range(line):
            solve()

if __name__=="__main__":
    main()

