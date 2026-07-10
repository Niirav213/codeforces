import sys

def solve():
    n = int(sys.stdin.readline())

    a = list(map(int, sys.stdin.readline().split()))

    new_a = []
    for x in a:
        if not new_a or x != new_a[-1]:
        
            new_a.append(x)
    m = len(new_a)
    if m <= 1:
        print(1)
        return
    

    ans = 2
    for i in range(1, m - 1):
        
        if (new_a[i] > new_a[i - 1] and new_a[i] > new_a[i + 1]) or (
            new_a[i] < new_a[i - 1] and new_a[i] < new_a[i + 1]
            ):
    
            ans += 1

    print(ans)
            
if __name__=="__main__":
    l = int(sys.stdin.readline())
    for _ in range(l):
        solve()