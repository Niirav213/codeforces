from re import M
import sys

def solve():
    m = sys.stdin.readline().split()
    n = int(m[0])
    z = str(m[1])

    s = sys.stdin.readline().strip()

    s += s
    n *= 2
    last_g = -1

    max_dist = -float('inf')

    for i in range(n-1, -1, -1):
        if s[i] == 'g':
            last_g = i
            
        if s[i] == z:
            max_dist = max(max_dist, last_g - i)
    
    
    print(max_dist)

def main():
    l = int(sys.stdin.readline().strip())

    if l:
        for _ in range(l):
            solve()


if __name__=="__main__":
    main()