import sys

def solve():
    n = int(sys.stdin.readline().strip())

    a = list(map(int,sys.stdin.readline().split()))

    
    c0 = a.count(0)
    c1 = a.count(1)
    c2 = a.count(2)

    pairs = min(c1,c2)
    leftovers = abs(c1 - c2)
    triplets = leftovers // 3
    print(pairs + triplets + c0)

def main():
    line = int(sys.stdin.readline().strip())
    if line:
        for _ in range(line):
            solve()

if __name__=="__main__":
    main()