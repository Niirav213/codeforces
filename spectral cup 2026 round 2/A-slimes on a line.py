import sys



def solve():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))

    arr.sort()

    steps = (arr[n-1] - arr[0] + 1) // 2
    print(steps)

def main():
    l = int(sys.stdin.readline())

    if l:
        for _ in range(l):
            solve()


if __name__=="__main__":
    main()