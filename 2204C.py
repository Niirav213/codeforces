import sys
from math import lcm

def get_one(a, m):
    return m // a


def get_two(a,b,m):
    return m // (lcm(a,b))

def get_three(a,b,c,m):
    return m // (lcm(a,b,c))

def get(a,b,c,m):
    c1 = get_one(a,m)
    c2 = get_two(a,b,m) + get_two(a,c,m)
    c3 = get_three(a,b,c,m)
    return (c1 - c2 + c3) * 6 + (c2 - 2 * c3) * 3 + c3 * 2

def solve():
    a,b,c,m = map(int, sys.stdin.readline().split())

    A = get(a,b,c,m)
    B = get(b,a,c,m)
    C = get(c,a,b,m)
    print(A,B,C)

    return

if __name__=="__main__":
    l = int(sys.stdin.readline())
    for _ in range(l):
        solve()