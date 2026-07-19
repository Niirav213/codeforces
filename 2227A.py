import sys

def solve():
    a,b =  map(int, sys.stdin.readline().split())

    if a & 1 != 0 and b & 1 != 0:
        print("NO")
    else:
        print("YES")

if __name__=="__main__":
    l = int(sys.stdin.readline())

    for _ in range(l):
        solve()