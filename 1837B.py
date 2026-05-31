import sys

def solve():

    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline()

    max_len = 0
    m=1
    for i in range(1,n):
        if s[i] == s[i-1]:
            m += 1

        else:
            max_len = max(max_len, m)
            m = 1
    max_len = max(max_len, m)
    
    print(max_len + 1)

def main():
    l = int(sys.stdin.readline())

    if l:
        for _ in range(l):
            solve()

if __name__=="__main__":
    main()