import sys

def solve():
    n,m = map(int, sys.stdin.readline().split())
    a = list(map(int,sys.stdin.readline().split()))

    a.sort()

    gaps = []

    for i in range(m-1):
        gaps.append(a[i+1] - a[i] - 1)
    gaps.append(a[0] + n - a[m-1] - 1)
    
    gaps.sort(reverse=True)

    num_saved = 0
    num_days = 0

    for gap in gaps:
        curr_gap = gap - num_days * 2
        if curr_gap > 0:
            num_saved += 1
            
            curr_gap -= 2
            if curr_gap > 0:
                num_saved += curr_gap
            num_days += 2
    print(n - num_saved)


if __name__=="__main__":
    l = int(sys.stdin.readline())

    for _ in range(l):
        solve()