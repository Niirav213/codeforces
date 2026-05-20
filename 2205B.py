import sys

def solve():
    n = int(sys.stdin.readline())
    k = 1
    d = 2
    temp = n
    while d*d <= temp :
        if temp % d == 0:
            k *= d
            while temp % d == 0:
                temp //= d
        d += 1
    if temp > 1:
        k *= temp
    print(k)

def main():
    l = int(sys.stdin.readline())
    if l:
        for _ in range(l):
            solve()


if __name__=="__main__":
    main()
