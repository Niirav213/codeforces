import sys

def solve():
    try:
        arr = sys.stdin.readline()
        arr = list(map(int, arr.split()))
        if not arr:
            return
    except ValueError:
        return
    
    total_sum  = sum(arr)
    max_val = max(arr)

    result = 2 * max_val - total_sum
    print(result)
    return

def main():
    num = int(sys.stdin.readline().strip())
    if num:
        for _ in range(num):
            solve()

if __name__=="__main__":
    main()