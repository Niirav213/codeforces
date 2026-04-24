import sys

def solve():
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().split()))

    if arr[0] == -1 and arr[n-1] != -1:
        arr[0] = arr[n-1]
    
    elif arr[0] != -1 and arr[n-1] == -1:
        arr[n-1] = arr[0]
    
    elif arr[0] == -1 and arr[n-1] == -1:
        arr[n-1] ,arr[0] = 0, 0

    for i in range(1,n-1):
        if arr[i] == -1:
            arr[i] = 0
    
    diff = abs(arr[n-1] - arr[0])
    print(diff)
    print(*(arr))

def main():
    line = int(sys.stdin.readline())
    if line:
        for _ in range(line):
            solve()

if __name__=="__main__":
    main()
    