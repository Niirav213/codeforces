import sys



def solve():
    w,h = map(int, sys.stdin.readline().split())

    x_down = list(map(int, sys.stdin.readline().split()))
    x_up = list(map(int, sys.stdin.readline().split()))

    y_left = list(map(int, sys.stdin.readline().split()))
    y_right= list(map(int, sys.stdin.readline().split()))


    x_max = max((x_down[x_down[0]] - x_down[1]), x_up[x_up[0]] - x_up[1])
    y_max = max((y_left[y_left[0]] - y_left[1]), (y_right[y_right[0]] - y_right[1]))

    ans = max(x_max*h, y_max*w)
    print(ans)

if __name__=="__main__":
    l = int(sys.stdin.readline().strip())

    for _ in range(l):
        solve()