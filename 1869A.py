import sys

def solve():
    n = int(sys.stdin.readline().strip())

    a = list(map(int, sys.stdin.readline().split()))

    if n & 1:
        print("4\n")
        sys.stdout.write(f"1 {n-1}\n")
        sys.stdout.write(f"1 {n-1}\n")
        sys.stdout.write(f"{n-1} {n}\n")
        sys.stdout.write(f"{n-1} {n}\n")
    
    else:
        sys.stdout.write("2\n")
        sys.stdout.write(f"1 {n}\n")
        sys.stdout.write(f"1 {n}\n")


def main():
    l = int(sys.stdin.readline().strip())
    for _ in range(l):
        solve()
    
if __name__=="__main__":
    main()