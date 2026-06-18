import sys


def solve():
    n,c = map(int, sys.stdin.readline().strip().split())

    s = list(map(int,sys.stdin.readline().strip().split()))

    right = 10**9
    left = 0
    while left <= right:
        mid = left + (right - left) // 2
        curr_sum = 0
        for i in range(n):
            curr_sum += (s[i] + 2*mid)**2
            if curr_sum > c:
                break
        if curr_sum == c:
            print(mid)
            return
            
        elif curr_sum < c:
            left = mid + 1
        else:
            right = mid - 1

if __name__=="__main__":
    l = int(sys.stdin.readline().strip())
    if l:
        for _ in range(l):
            solve()

