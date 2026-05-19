import sys

def solve():
    n,a,b = map(int, sys.stdin.readline().split())

    cost1 = n * a
    cost2 = (n//3)* b + (n%3)*a
    cost3 = ((n+2)//3) * b
    print(min(cost1, cost2, cost3))

def main():
    line = int(sys.stdin.readline())
    if line:
        for _ in range(line):
            solve()

if __name__=="__main__":
    main()