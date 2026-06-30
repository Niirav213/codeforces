import sys


def solve():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()

    change = 0
    for i in range(1,n):
        if s[i] != s[i-1]:
            change += 1
    
    if change == 1:
        print(2)
    else:
        print(1)

if __name__=="__main__":
    l = int(sys.stdin.readline())
    for _ in range(l):
        solve()