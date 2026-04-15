import sys

def solve():
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().split()))

    if not arr:
        return
    
    is_sorted = True

    for i in range(n-1):
        if arr[i] > arr[i + 1]:
            is_sorted = False
            break
    
    if is_sorted:
        print(n)
    else:
        print(1)

def main():
    n = int(sys.stdin.readline().strip())
    if not n:
        return
    for _ in range(n):
        solve()

if __name__=="__main__":
    main()