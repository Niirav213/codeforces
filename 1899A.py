import sys

def solve():
    n = int(sys.stdin.readline())

    if n % 3 == 1 or n % 3 == 2:
        print("First")
    
    else:
        print("Second")


def main():
    l = int(sys.stdin.readline())

    if l:
        for _ in range(l):
            solve()


if __name__=="__main__":
    main()