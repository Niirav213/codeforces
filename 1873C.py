import sys

points_array = [[1,1,1,1,1,1,1,1,1,1],
                [1,2,2,2,2,2,2,2,2,1],
                [1,2,3,3,3,3,3,3,2,1],
                [1,2,3,4,4,4,4,3,2,1],
                [1,2,3,4,5,5,4,3,2,1],
                [1,2,3,4,5,5,4,3,2,1],
                [1,2,3,4,4,4,4,3,2,1],
                [1,2,3,3,3,3,3,3,2,1],
                [1,2,2,2,2,2,2,2,2,1],
                [1,1,1,1,1,1,1,1,1,1]]


def solve():
    ans = 0
    for i in range(10):
        r = sys.stdin.readline()
        for j in range(10):
            if r[j] == 'X':
                ans += points_array[i][j]

    print(ans)


def main():
    l = int(sys.stdin.readline().strip())

    if l:
        for _ in range(l):
            solve()

if __name__=="__main__":
    main()