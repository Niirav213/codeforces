import sys

def solve():
    a, b = map(int, sys.stdin.readline().split())

    xk, yk = map(int, sys.stdin.readline().split())

    xq, yq = map(int, sys.stdin.readline().split())

    king_side = []
    king_side.append((xk - a, yk-b))
    king_side.append((xk - b, yk-a))
    king_side.append((xk + a, yk+b))
    king_side.append((xk + b, yk+a))
    king_side.append((xk + a, yk-b))
    king_side.append((xk - a, yk+b))
    king_side.append((xk + b, yk-a))
    king_side.append((xk - b, yk + a))

    queen_side = []
    queen_side.append((xq + a, yq + b))
    queen_side.append((xq + a, yq - b))
    queen_side.append((xq - a, yq + b))
    queen_side.append((xq - a, yq - b))
    queen_side.append((xq + b, yq + a))
    queen_side.append((xq + b, yq - a))
    queen_side.append((xq - b, yq + a))
    queen_side.append((xq - b, yq - a))

    ans = list(set(king_side) & set(queen_side))

    print(len(ans))

def main():
    l = int(sys.stdin.readline().strip())

    for _ in range(l):
        solve()

if __name__=="__main__":
    main()