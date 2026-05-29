import sys

def solve():
    n,k,x = map(int, sys.stdin.readline().split())

    
    min_sum = k * (k + 1) // 2

    max_sum = k * (2 * n - k + 1) // 2

    if x<= max_sum and x >= min_sum:
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