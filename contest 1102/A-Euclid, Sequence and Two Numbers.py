import sys


def solve():
    n = int(sys.stdin.readline().strip())

    b = list(map(int, sys.stdin.readline().split()))


    b.sort(reverse=True)

    for i in range(2, n):
        if b[i] != b[i-2] % b[i-1]:
            print(-1)
            return
    
    print(b[0], b[1])


def main():
    l = int(sys.stdin.readline().strip())

    if l:
        for _ in range(l):
            solve()


if __name__=="__main__":
    main()