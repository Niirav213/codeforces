import sys
import math

def solve():
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))
    
    ans = 0
    # We only need to loop up to the middle of the array to check symmetric pairs
    for i in range(n // 2):
        diff = abs(a[i] - a[n - 1 - i])
        ans = math.gcd(ans, diff)
        
    print(ans)

if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        solve()
