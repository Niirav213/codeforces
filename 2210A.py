import sys

def solve():
    n = int(sys.stdin.readline().strip())

    perm = []
    perm.append(n-1)
    perm.append(n)

    for i in range(n-2, 0, -1):
        perm.append(i)

    print(*(perm))

def main():
    line = int(sys.stdin.readline().strip())
    if line:
        for _ in range(line):
            solve()

if __name__=="__main__":
    main()