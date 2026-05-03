import sys

def solve():
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().split()))

    arr.sort(reverse=True)

    a = 1
    for i in range(1,n):
        if arr[i] != arr[i-1]:
            break
        else:
            a += 1
    
    print(a)

def main():
    line  = int(sys.stdin.readline())
    if line:
        for _ in range(line):
            solve()


if __name__=="__main__":
    main()