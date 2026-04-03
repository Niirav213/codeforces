import sys
def solve():
    try:
        x = int(sys.stdin.readline().strip())
        if not x:
            return
    
    except ValueError:
        return
    
    if x % 9 != 0:
        print('0')
        return
    
    count = 0
    for y in range(x, x + 100):
        digit_sum = sum(int(d) for d in str(y))
        if y - digit_sum == x:
            count += 1
    print(count)
    return

def main():
    n = int(sys.stdin.readline().strip())
    if not n:
        return
    for _ in range(n):
        solve()
    
if __name__=="__main__":
    main()