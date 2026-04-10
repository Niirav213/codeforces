import sys

def solve():
    try:
        len = int(sys.stdin.readline().strip())
        arr = list(map(int, sys.stdin.readline().split()))
        if not len:
            return
    except ValueError:
        return
    
    dict = []
    for i in range(len):
        dict.append((arr[i], i))

    dict.sort()

    same_parity = True
    diff_parity = True
    for i in range(len):
        original = dict[i][1]

        if i % 2 != original % 2:
            same_parity = False

        if i % 2 == original % 2:
            diff_parity = False

    if same_parity or diff_parity:
        print("YES")
    else:
        print("NO")


def main():
    n = int(sys.stdin.readline().strip())
    if n:
        for _ in range(n):
            solve()

if __name__=="__main__":
    main()