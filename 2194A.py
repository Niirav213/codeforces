import sys

def solve():
    test = sys.stdin.readline().strip()
    x = list(map(int, test.split()))

    mover = x[1]
    fence = x[0]
    
    ans = fence - (fence // mover)
    print(ans)
    return


def main():
    line = int(sys.stdin.readline().strip())
    if line:
        for _ in range(line):
            solve()

if __name__=="__main__":
    main()