import sys
from math import lcm
def solve():
    n,x,y = map(int,sys.stdin.readline().split())

    sum = 0
    sub = 0
    GCD = lcm(x,y)
    overlap = n // GCD
    c1 = n//x- overlap
    c2 = n//y- overlap

    sum = (n-c1+1 + n) * (c1) // 2
    sub = (1 + c2)* (c2) //2 

    ans = sum -sub
    print(ans)

if __name__=="__main__":
    l = int(sys.stdin.readline())

    for _ in range(l):
        solve()