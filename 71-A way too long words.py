import sys
def solve():
    try:
        s = sys.stdin.readline().strip()
        if not s:
            return
    except ValueError:
        return
    length = len(s)
    if length > 10:
        print(s[0] + f'{length - 2}'+ s[length-1])
        return
    print(s)
    return

def main():
    a = int(sys.stdin.readline().strip())
    if not a:
        return
    
    for _ in range(a):
        solve()

if __name__=="__main__":
    main()