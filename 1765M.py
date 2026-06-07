import sys
import math
def solve():
    n = int(sys.stdin.readline().strip())

    ans_a = 1
    ans_b = n-1

    for i in range(2,int(math.sqrt(n))+ 1):
        if n % i == 0:
            ans_a = n//i
            ans_b = n - ans_a
            break
    


    print(ans_a, ans_b)

def main():
    l = int(sys.stdin.readline())
    if l:
        for _ in range(l):
            solve()


if __name__=="__main__":
    main()