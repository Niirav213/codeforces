import sys

def solve():
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))

    total = sum(a)

    if total % 2 == 1 or (n * k) % 2 == 0:
        print("YES")
    else:
        print("NO")

def main():
    line = int(sys.stdin.readline().strip())
    if line:
        for _ in range(line):
            solve()

if __name__=="__main__":
    main()