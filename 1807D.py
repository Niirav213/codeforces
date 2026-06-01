import sys

def solve():
    n, q = map(int ,sys.stdin.readline().split())

    a = list(map(int, sys.stdin.readline().split()))
    old_sum = sum(a)

    prefix_sum = [0] * (n+ 1)
    for i in range(1, n+1):
        prefix_sum[i] = prefix_sum[i-1] + a[i-1]
    
    result = []

    for _ in range(q):
        l,r,k = map(int, sys.stdin.readline().split())
        removed_sum = prefix_sum[r] - prefix_sum[l-1]
        sum_of_k = k*(r-l+ 1)
        total_sum = old_sum - removed_sum + sum_of_k
    
        if total_sum % 2 == 1:
            result.append("YES")
        else:
            result.append("NO")
    print("\n".join(result))

def main():
    l = int(sys.stdin.readline().strip())

    if l:
        for _ in range(l):
            solve()

if __name__=="__main__":
    main()
