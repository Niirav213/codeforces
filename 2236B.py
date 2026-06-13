import sys

def solve():
    n,k = map(int,(sys.stdin.readline().split()))

    
    a = sys.stdin.readline().strip()
    
    count_ones = [0] * n
    for i in range(n):
        if a[i] == '1':
            count_ones[i % k ] += 1

    for i in count_ones:
        if i % 2 != 0:
            print("NO")
            return 
    print("YES")
if __name__=="__main__":
    l = int(sys.stdin.readline())
    if l:
        for _ in range(l):
            solve()

