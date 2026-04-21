import sys

def solve():
    n = int(sys.stdin.readline().strip())
    perm = [0] + list(map(int, sys.stdin.readline().split()))

    for i in range(1,n+1):
        idx_perm = i
        while idx_perm % 2 == 0:
            idx_perm //= 2
        val_temp = perm[i]
        while val_temp % 2 == 0:
            val_temp //= 2
        
        if idx_perm != val_temp:
            print("NO")
            return
    
    print("YES")
    return

def main():
    line = int(sys.stdin.readline().strip())
    if line:
        for _ in range(line):
            solve()

if __name__=="__main__":
    main()