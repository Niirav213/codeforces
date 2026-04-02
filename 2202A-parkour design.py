import sys

def solve():
    try:
        cord = sys.stdin.readline().split()
        if not cord:
            return
    except ValueError:
        return
    
    x = int(cord[0].strip())
    y = int(cord[1].strip())
    
    if (x - 2*y) % 3 == 0 and x >= 2*y and x >= -4*y:
        print("YES")
        return
    else:
        print("NO")
        return

def main():
    line = sys.stdin.readline()

    if line:
        n = int(line.strip())
        for _ in range(n):
            solve()

if __name__=="__main__":
    main()


