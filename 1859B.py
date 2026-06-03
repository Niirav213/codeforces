import sys


def solve():
    n = int(sys.stdin.readline().strip())
    least = float('inf')
    second_least = []
    for _ in range(n):
        m = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().split()))

        a.sort()
        least = min(least, a[0])
        second_least.append(a[1])
    second_least.sort()
    k = sum(second_least)
    s = second_least[0]
    print(least + k - s)

def main():
    l = int(sys.stdin.readline())
    if l:
        for _ in range(l):
            solve()

if __name__=="__main__":
    main()