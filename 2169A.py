import sys
from bisect import bisect_left, bisect_right

def solve():
    n,a = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))

    l_count = bisect_left(arr, a)

    r_count = n - bisect_right(arr, a)

    if l_count > r_count:
        print(a-1)
    elif l_count < r_count:
        print(a+1)
    else:
        print(a+1)


def main():
    line = int(sys.stdin.readline().strip())
    if line:
        for _ in range(line):
            solve()

if __name__=="__main__":
    main()