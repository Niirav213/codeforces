import sys

def solve():
    try:
        line1 = sys.stdin.readline()
        if not line1:
            return
        n = int(line1.strip())
        s = sys.stdin.readline()
    except ValueError:
        return
    
    for i in range(n):
        if (n-1-i) % 2 == 0:
            target_idx = (n+1+i)//2
            required_char = 'a' if target_idx % 2 != 0 else 'b'

            if s[i] != '?' and s[i] != required_char:
                print("No")
                return
    print("Yes")

def main():
    line = sys.stdin.readline()
    if line:
        t = int(line.strip())
        for _ in range(t):
            solve()

if __name__=='__main__':
    main()