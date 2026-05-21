import sys

def solve():
    x = int(sys.stdin.readline())

    y = 2*x

    print(y)

def main():
    line = int(sys.stdin.readline())

    if line:
        for _ in range(line):
            solve()

if __name__=="__main__":
    main()
