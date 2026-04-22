import sys

def solve():
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().split()))

    u = sorted(list(set(arr)))
    m = len(u)

    max_run = 1
    current_run = 1

    for i in range(1,m):
        if u[i] == u[i-1] + 1:
            current_run += 1
        else:
            current_run = 1
        
        if current_run > max_run:
            max_run = current_run
    print(max_run)

def main():
    line = int(sys.stdin.readline().strip())

    if line:
        for _ in range(line):
            solve()

if __name__=="__main__":
    main()