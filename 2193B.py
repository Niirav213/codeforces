import sys

def solve():
    n = int(sys.stdin.readline())
    p = list(map(int, sys.stdin.readline().split()))

    target_idx = -1
    for i in range(n):
        if p[i] != n - i:
            target_idx = i
            break
    if target_idx == -1:
        print(*(p))
        return
    
    wanted_val = n - target_idx
    val_idx = -1

    for j in range(target_idx, n):
        if p[j] == wanted_val:
            val_idx = j
            break

    segment = p[target_idx: val_idx + 1]
    segment.reverse()

    result = p[:target_idx] + segment + p[val_idx + 1:]
    print(*(result))


def main():
    line = sys.stdin.readline()
    if not line:
        return
    for _ in range(int(line)):
        solve()

if __name__=="__main__":
    main()