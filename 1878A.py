import sys

def solve():
    n,k = map(int, sys.stdin.readline().split())

    a = list(map(int, sys.stdin.readline().split()))
    
    
    
    if k in a:
        print("YES")
    else:
        print("NO")


def main():
    l = int(sys.stdin.readline().strip())

    if l:
        for _ in range(l):
            solve()

if __name__=="__main__":
    main()