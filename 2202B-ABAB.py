import sys

def solve():
    try:
        line1 = sys.stdin.readline()
        if not line1:
            return
        n = int(line1.strip())
        s = sys.stdin.readline().strip()
    except ValueError:
        return
    
    #for odd lenght
    if(n&1):
        if s[0] == 'b':
            print("No")
            return
        for i in range(1,n - 1, 2):
            if s[i] != s[i+1] or s[i] == '?' or s[i+1] == '?': continue
            else:
                print("No")
                return
    else:
        for i in range(0, n - 1 , 2 ):
            if s[i] != s[i+1] or s[i] == '?' or s[i+1] == '?': continue
            else:
                print("No")
                return
    print("yes")

def main():
    line = sys.stdin.readline()
    if line:
        t = int(line.strip())
        for _ in range(t):
            solve()

if __name__=='__main__':
    main()