import sys

def solve():
    s = list(sys.stdin.readline().strip())

    ans = 0
    r = len(s)
    if s[0] == 'u':
        ans += 1
        s[0] = 's'
    if s[r-1] == 'u':
        ans += 1
        s[r-1] = 's'
    
    i = 0
    while i < r:
        if s[i] == 'u':
            count = 0
            while i<r and s[i] == 'u':
                count += 1
                i += 1
            ans += count // 2
        else:
            i += 1
    print(ans)


def main():
    line = int(sys.stdin.readline().strip())

    if line:
        for _ in range(line):
            solve()

if __name__=="__main__":
    main()