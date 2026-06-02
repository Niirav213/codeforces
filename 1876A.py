import sys

def solve():
    n,p = map(int, sys.stdin.readline().split())

    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))

    my_dict = [(b[i], a[i]) for i in range(n)]

    my_dict.sort()

    min_cost = p
    shared = 1

    for sharing_cost, max_share in my_dict:
        if sharing_cost >= p:
            break

        if shared + max_share > n:
            min_cost += (n - shared) * sharing_cost
            shared = n
            break
        else:
            min_cost += max_share * sharing_cost
            shared += max_share

    
    min_cost += (n - shared) * p

    print(min_cost)

def main():
    l = int(sys.stdin.readline())
    if l:
        for _ in range(l):
            solve()

if __name__=="__main__":
    main()