import sys

def solve():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    ans = []
    par = 0
    for i in range(n-1,-1,-1):
        if par == 1:
            a[i] = -a[i]
        if a[i] > 0:
            ans.append(i)
            par ^= 1
    
    print(len(ans),"\n", *(i+1 for i in ans))


def main():
    l= int(sys.stdin.readline())
    if l:
        for _ in range(l):
            solve()

if __name__=="__main__":
    main()