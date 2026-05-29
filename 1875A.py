import sys


def solve():
    a,b,n = map(int, sys.stdin.readline().split())
    x = list(map(int, sys.stdin.readline().split()))

    seconds = b
    for i in x:
        seconds += min(i, a-1)
        
    print(seconds)

def main():
    l = int(sys.stdin.readline().strip())
    if l:
        for _ in range(l):
            solve()


if __name__=="__main__":
    main()