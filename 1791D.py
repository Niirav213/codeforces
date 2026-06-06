import sys

def solve():
    n = int(sys.stdin.readline().strip())

    s = sys.stdin.readline().strip()
    
    st = set()
    suf_cnt= [0] * (n+1)
    pref_cnt = [0] * (n+1)

    for i in range(1,n+1):
        st.add(s[i-1])
        pref_cnt[i] = len(st)
    
    st.clear()

    for i in range(n,0,-1):
        st.add(s[i-1])
        suf_cnt[i] = len(st)
    ans = 0

    for i in range(n):
        ans = max(ans, pref_cnt[i] + suf_cnt[i+1])
    
    print(ans)


def main():
    l = int(sys.stdin.readline())
    if l:
        for _ in range(l):
            solve()


if __name__=="__main__":
    main()