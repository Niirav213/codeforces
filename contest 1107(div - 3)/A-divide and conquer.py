import sys

def solve():
    x,y = map(int, sys.stdin.readline().split())

    if x % y == 0:
        print("YES")
    else:
        print("NO")

if __name__=="__main__":
    l = int(sys.stdin.readline())
    for _ in range(l):
        solve()