import sys

def solve():
    n = int(sys.stdin.readline())

    a = list(map(int, sys.stdin.readline().split()))

    for i in range(n):
        if a[i] == 1:
            a[i] += 1
    for i in range(n-1):
        if a[i+1] % a[i] == 0:
            a[i+1] += 1
    
    print(*(a))

def main():
    l = int(sys.stdin.readline())
    if l:
        for _ in range(l):
            solve()

if __name__=="__main__":
    main()