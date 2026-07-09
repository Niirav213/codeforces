import heapq
import sys


def solve():
    n,k = map(int, sys.stdin.readline().split())

    c = list(map(int,sys.stdin.readline().split()))

    colors = [[] for _ in range(k+1)]



    for i in range(1, k + 1):    
        colors[i].append(0)
    
    for i in range(n):

        colors[c[i]].append(i+1)


    for i in range(1, k+1):
        colors[i].append(n+1)
    jumps = [[] for _ in range(k+1)]

    ans = float('inf')

    for i in range(1, k+1):
        for j in range(len(colors[i]) - 1):
            jump_len = colors[i][j+1] - colors[i][j] - 1
            heapq.heappush(jumps[i], -jump_len)
        max_val = -heapq.heappop(jumps[i])

        if max_val % 2==0:
            heapq.heappush(jumps[i], -(max_val // 2))
            heapq.heappush(jumps[i], -(max_val//2 - 1))
        else:
            heapq.heappush(jumps[i], -(max_val // 2))
            heapq.heappush(jumps[i], -(max_val // 2))
        
        ans =  min(ans, -jumps[i][0])
    print(ans)
    return

if __name__=="__main__":
    l = int(sys.stdin.readline())

    for _ in range(l):
        solve()