import sys

def solve():
    try:
        x = sys.stdin.readline().strip()
        if not x:
            return
    except ValueError:
        return
    x = int(x)
    if x == 67:
        print(x)
        return
    else:
        print(x + 1)
        return
    
def main():
    num = int(sys.stdin.readline().strip())
    
    if not num:
        return
    for _ in range(num):
        solve()

if __name__=="__main__":
    main()