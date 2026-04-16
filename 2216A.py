import sys

def solve():
    n,k = map(int, (sys.stdin.readline().split()))
    cap = list(map(int,(sys.stdin.readline().split())))
    wish = list(map(int,(sys.stdin.readline().split())))

    ans = []

    while any(level < k + 1 for level in wish):
        moved = False

        for j in range(k, 0, -1):
            for i in range(n):
                if wish[i] == j:
                    k1 = j + 1

                    if k1 == k + 1:
                        wish[i] += 1
                        ans.append(i + 1)
                        moved = True
                        break
                    else:
                        curr_count = wish.count(k1)
                        if curr_count < cap[k1 - 1]:
                            wish[i] += 1
                            ans.append(i + 1)
                            moved = True
                            break
            if moved: break
    print(len(ans))
    print(*(ans))

def main():
    line = int(sys.stdin.readline())
    if line:
        for _ in range(line):
            solve()

if __name__=="__main__":
    main()