import sys

def solve():
    n,x,y,z = map(int, sys.stdin.readline().split())

    numerator_ai = 10 * z * y + n
    denominator_ai = x + 10 * y
    using_ai = (numerator_ai + denominator_ai - 1) // denominator_ai

    numerator_not_ai = n
    denominator_not_ai = x + y
    not_using_ai = (numerator_not_ai + denominator_not_ai - 1) // denominator_not_ai

    print(min(using_ai, not_using_ai))

if __name__=="__main__":
    l = int(sys.stdin.readline().strip())
    if l:
        for _ in range(l):
            solve()