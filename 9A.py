import sys
from fractions import Fraction
def solve():
    die =  list(map(int,sys.stdin.readline().split()))

    m = max(die)
    numerator =  7 - m
    ans = Fraction(numerator, 6)
    if ans == 1:
        ans = "1/1"
    print(ans)   
    
    
    

if __name__=="__main__":
    solve()

