import sys

def solve():
    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()

    if n % 2 != 0:
        print("NO")
        return
    stack = []

    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    if not stack:
        print("YES")
    else:
        print("NO")

def main():
    line = int(sys.stdin.readline().strip())
    if line:
        for _ in range(line):
            solve()

if __name__=="__main__":
    main()