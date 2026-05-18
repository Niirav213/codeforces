import sys

def solve():
    n,x1,x2,k = map(int , sys.stdin.readline().split())

    if n<=3:
        print('1')
    else:
        print(min(abs(x1-x2), n - abs(x1-x2)) + k)

def main():
    l = int(sys.stdin.readline().strip())
    if l:
        for _ in range(l):
            solve()

if __name__=="__main__":
    main()