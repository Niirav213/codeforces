import sys


def solve():
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().split()))

    ans = []
    if n == 1:
        print(1)
        return

    else:
        for i in range(n):
            ans.append(2)
        print(*(ans))
        return
def main():
    line = int(sys.stdin.readline().strip())

    if line:
        for _ in range(line):
            solve()

if __name__=="__main__":
    main()

