import bisect
import sys


def main():
    n = int(sys.stdin.readline().strip())
    a = sorted(list(map(int, sys.stdin.readline().split())))
    b = sorted(list(map(int, sys.stdin.readline().split())),reverse=True)
    MOD = 10**9 + 7
    result = 1
    for i in range(n):
        geq = n - bisect.bisect_right(a, b[i])
        result = result * max(geq - i, 0) % MOD
    
    print(result)

if __name__=="__main__":
    l = int(sys.stdin.readline().strip())
    for _ in range(l):
        main()