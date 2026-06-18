import sys

def check(mid,heights, x):
    units = 0
    n = len(heights)
    for i in range(n):
        if heights[i] < mid:
             units += (mid - heights[i])
    return units<= x

def main():
    n,x = map(int, sys.stdin.readline().split())

    a = list(map(int, sys.stdin.readline().strip().split()))

    l, r = 1, int(1e12)
    ans = -1

    while l<=r:
        mid = l + (r-l ) // 2
        if check(mid,a,x):
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    
    print(ans)

if __name__=="__main__":
    l = int(sys.stdin.readline())
    for _ in range(l):
        main()
