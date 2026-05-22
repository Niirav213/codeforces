import sys

def solve():
    n = int(input())
    a = []
    v = 1
    while len(a) < n:
        a.append(v)
        if len(a) < n:
            a.append(v + 1)
        v += 3
    print(*a)

def main():
    l = int(sys.stdin.readline())
    if l:
        for _ in range(l):
            solve()

if __name__=="__main__":
    main()
