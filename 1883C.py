import sys

def solve():
    n,k = map(int, sys.stdin.readline().split())

    a = list(map(int, sys.stdin.readline().split()))

    ans = float('inf')

    even_count = 0

    for i in a:
        if i % 2 == 0:
            even_count += 1
        if i % k == 0:
            ans = 0

        ans = min(ans, (k - i % k))
    
    if k ==4:
        if even_count >= 2:
            ans = min(ans, 0)
        elif even_count == 1:
            ans = min(ans, 1)
        elif even_count == 0:
            ans = min(ans,2)
    print(ans)


def main():
    l = int(sys.stdin.readline())

    if l:
        for _ in range(l):
            solve()


if __name__=="__main__":
    main()