import sys

def solve():
    n,x,y = map(int, sys.stdin.readline().split())

    s = sys.stdin.readline()

    coutn8 = s.count('8')
    
    dist_max = max(abs(x), abs(y))

    dist_sum = abs(x) + abs(y)

    if dist_max <= n and dist_sum <= n + coutn8:
        print('YES')
    else:
        print("NO")

def main():
    line = int(sys.stdin.readline())
    if line:
        for _ in range(line):
            solve()

if __name__=="__main__":
    main()