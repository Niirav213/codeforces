import sys

def solve():
    n, m = map(int, sys.stdin.readline().split())

    available = [False] * 26
    for _ in range(n):
        s = sys.stdin.readline().strip()
        available[ord(s[0]) - ord("a")] = True

    ok = True

    for _ in range(m):
        abb = sys.stdin.readline().strip()

        for c in abb:
            if not available[ord(c) - ord('A')]:
                ok = False

    if ok:
        print("YES")
    else:
        print("NO")

    
if __name__=="__main__":
    l = int(sys.stdin.readline())
    for _ in range(l):
        solve()    


