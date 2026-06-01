import sys
import math

def solve():
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().split()))

    k = abs(a[0] - 1)

    for i in range(1,n):
        k = math.gcd(k, abs(a[i] - i - 1))
    print(k)
   
def main():
    l = int(sys.stdin.readline().strip())
    if l:
        for _ in range(l):
            solve()

if __name__=="__main__":
    main()