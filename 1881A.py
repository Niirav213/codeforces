
import sys

def solve():
    n,m = map(int, sys.stdin.readline().split())

    x = sys.stdin.readline().strip()
    s= sys.stdin.readline().strip()
    

    for i in range(6):
        if s in x:
            print(i)
            return
        x += x
    
    print("-1")

def main():
    l = int(sys.stdin.readline())

    if l:
        for _ in range(l):
            solve()

if __name__=="__main__":
    main()