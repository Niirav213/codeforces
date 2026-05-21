import sys

def solve():
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline()
    ans = 0
    for i in range(n):
        ans += 1
        if arr[i] == 'L':
            break
    print(ans)

def main():
    l = int(sys.stdin.readline())
    if l:
        for _ in range(l):
            solve()
    
if __name__=="__main__":
    main()