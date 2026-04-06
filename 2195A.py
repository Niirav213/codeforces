import sys

def solve():
    try:
        length = int(sys.stdin.readline().strip())
        arr = sys.stdin.readline()
        arr = list(map(int, arr.split()))
        if not arr:
            return
    except ValueError:
        return
    
    for i in range(length):
        for j in range(length):
            if arr[i] * arr[j] == 67 or arr[i] == 67 or arr[j] == 67:
                print("YES")
                return
    
    print("NO")
    return

def main():
    n = int(sys.stdin.readline().strip())
    if n:
        for _ in range(n):
            solve()


if __name__=="__main__":
    main()