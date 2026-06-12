import sys


def solve():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()

    freq = {}
    count = 0

    distinct = [0]*n

    for i in range(n):
        freq[s[i]] = freq.get(s[i], 0) + 1
    
        if freq[s[i]] == 1:
            count += 1
        distinct[i] = count


    ans = sum(distinct)
    print(ans)

    
if __name__=="__main__":
    l = int(sys.stdin.readline())
    if l:
        for _ in range(l):

            solve()

