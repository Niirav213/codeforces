import sys

def solve():
    n = (sys.stdin.readline().strip())
    ans = 0
    pref2 = 0
    suff = 0
    for x in n:
        if x == '1' or x == '3':
            suff += 1
    ans = pref2 + suff
    for x in n:
        if x == '2':
            suff += 1
        if x == '1' or x == '3':
            pref2 -= 1
        ans = max(ans , suff + pref2)
    
    print(len(n) - ans)

if __name__=="__main__":
    l = int(sys.stdin.readline())
    for _ in range(l):
        solve()