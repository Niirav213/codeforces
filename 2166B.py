import sys

def solve():
    a,b,n = map(int, sys.stdin.readline().split())

    if n * b <= a or b >= a:
        print(1)
    else:
        print(2)

def main():
    line = int(sys.stdin.readline().strip())

    if line:
        for _ in range(line):
            solve()


if __name__=="__main__":
    main()