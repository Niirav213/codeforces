import sys

def solve():
    n,c,k = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))

    arr.sort()

    for i in range(n):
        if arr[i] <= c:
            add = min(k, c - arr[i])

            eff = arr[i] + add
            k -= add
            c += eff
        else:
            break
            
    print(c)

def main():
    line = int(sys.stdin.readline().strip())

    if line:
        for _ in range(line):
            solve()

if __name__=="__main__":
    main()