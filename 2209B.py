import sys

def solve():
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().split()))

    ans = [0] * (n)
    
    for i in range(n):
        count1, count2 = 0, 0
        for j in range(i, n):
            if arr[j] > arr[i]:
                count1 += 1
            if arr[j] < arr[i]:
                count2 += 1
        ans[i] = max(count1,count2)

    print(*(ans))


def main():
    line = int(sys.stdin.readline().strip())
    if line:
        for _ in range(line):
            solve()

if __name__=="__main__":
    main()