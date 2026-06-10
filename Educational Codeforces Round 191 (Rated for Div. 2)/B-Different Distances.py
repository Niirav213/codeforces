import sys

def solve():
    n = int(sys.stdin.readline())

    print(n, end=" ")


    for i in range(1, n + 1):
        print(f"{i} {i}", end=" ")


    for i in range(1, n + 1):
        print(i, end=" ")


    for i in range(1, n):
        print(i, end=" ")
    print()


if __name__=="__main__":
    l = int(sys.stdin.readline())
    if l:
        for _ in range(l):
            solve()