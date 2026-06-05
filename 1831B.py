import sys

def solve():
    n = int(sys.stdin.readline())
    a = list(map(int,sys.stdin.readline().split()))
    b = list(map(int,sys.stdin.readline().split()))

    curr_lenA = 1
    curr_lenB = 1
    maxA = {}
    maxB = {}

    for i in range(1, n):
        if a[i] == a[i-1]:
            curr_lenA += 1
        else:
            maxA[a[i- 1]] = max(maxA.get(a[i-1], 0),curr_lenA)
            curr_lenA = 1
        
        if b[i] == b[i-1]:
            curr_lenB += 1

        else:
            maxB[b[i-1]] = max(maxB.get(b[i-1], 0), curr_lenB)
            curr_lenB = 1
    maxA[a[n-1]] = max(maxA.get(a[n-1], 0), curr_lenA)
    maxB[b[n-1]] = max(maxB.get(b[n-1], 0), curr_lenB)
    
    ans = 1

    all_elements = set(a).union(b)

    for element in all_elements:
        ans = max(ans, maxA.get(element, 0) + maxB.get(element, 0))

    print(ans)

def main():
    l = int(sys.stdin.readline())
    if l:
        for _ in range(l):
            solve()

if __name__=="__main__":
    main()