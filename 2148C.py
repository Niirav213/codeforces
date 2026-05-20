import sys

def solve():
    n, m = map(int, sys.stdin.readline().split())
    req, state = 0,0
    points = 0
    for i in range(n):
        
        a,b = map(int, sys.stdin.readline().split())
        dt = a - req
        need_flip = 1 if (state != b) else 0

        if (dt % 2) != need_flip:
            points += (dt - 1)
        else:
            points += dt
        
        req = a
        state = b
    points += (m - req)
    print(points)

def main():
    line = int(sys.stdin.readline())
    if line:
        for _ in range(line):
            solve()

if __name__=="__main__":
    main()
        
    
        
