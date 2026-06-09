import sys

def solve():
    n, d = map(int, sys.stdin.readline().split())

    a = list(map(int,(sys.stdin.readline().split())))

    a.sort()

    wins = 0
    len = 1

    left = -1
    right = n-1

    while left < right:
        if a[right] * len <= d and left < right:
            len += 1
            left += 1
        else:
            len = 1
            wins += 1
            right -= 1
    
    print(wins)

if __name__=="__main__":
    solve()
    

