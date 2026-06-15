from re import L
import sys

def solve():
    n = int(sys.stdin.readline())

    a = list(map(int, sys.stdin.readline().split()))

    l =0
    r =0
    curr_sum = 0 
    max_sum = -float('inf')
    while r<n:
        if curr_sum < 0:
            curr_sum = 0
            l = r
        if l < r:
            if (a[r] - a[r-1])& 1 != 0:
                curr_sum += a[r]
                
            else:
                curr_sum = a[r]
                l = r        
        else:
            curr_sum = a[r]
        max_sum = max(max_sum, curr_sum)
        r += 1

    print(max_sum)


if __name__=="__main__":
    l = int(sys.stdin.readline())
    for _ in range(l):
        solve()

