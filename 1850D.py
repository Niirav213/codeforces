import sys

def solve():
    n, k = map(int, sys.stdin.readline().split())

    a = list(map(int , sys.stdin.readline().split()))


    a.sort()
    temp = 1
    j = 1
    total = 1


    for i in range(n-1):
        if abs(a[i] - a[j]) <= k:
            temp += 1
        else:
            temp = 1
        total = max(total, temp)
        j += 1        

    print(n - total)


def main():
    l = int(sys.stdin.readline())

    if l:
        for _ in range(l):
            solve()

if __name__=="__main__":
    main()