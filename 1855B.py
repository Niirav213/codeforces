import sys

def solve():
    n = int(sys.stdin.readline().strip())
    i = 1
    while n % i == 0:
        i += 1

    sys.stdout.write(f"{i-1}\n")

def main():
    l = int(sys.stdin.readline().strip())

    if l:
        for _ in range(l):
            solve()

if __name__=="__main__":
    main()