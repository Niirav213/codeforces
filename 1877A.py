import sys

def solve():

    n = int(sys.stdin.readline())

    a = list(map(int, sys.stdin.readline().split()))

    a_sum = sum(a)

    print(-a_sum)


def main():
    l = int(sys.stdin.readline().strip())


    if l:
        for _ in range(l):
            solve()


if __name__=="__main__":
    main()