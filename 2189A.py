import sys

def solve():
    n,h,l = map(int, sys.stdin.readline().strip().split())
    arr = list(map(int, sys.stdin.readline().split()))

    count_h = 0  # Elements that can be rows
    count_l = 0  # Elements that can be columns
    count_useful = 0 # Elements that can be either a row or a column
    
    for x in arr:
        is_h = (x <= h)
        is_l = (x <= l)
        
        if is_h:
            count_h += 1
        if is_l:
            count_l += 1
        if is_h or is_l:
            count_useful += 1
    ans = min(count_h, count_l, count_useful // 2)
    print(ans)
    return

def main():
    try:
        line = int(sys.stdin.readline().strip())
        if not line:
            return
    except ValueError:
        return
    if line:
        for _ in range(line):
            solve()

if __name__=="__main__":
    main()