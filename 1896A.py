import sys

def solve():
    n = int(sys.stdin.readline())

    a = list(map(int, sys.stdin.readline().split()))

    if a[0] == 1:
        print("YES")
    
    else:
        print("NO")


def main():
    l = int(sys.stdin.readline())

    if l:
        for _ in range(l):
            solve()


if __name__=="__main__":
    main()