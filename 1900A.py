import sys


def solve():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline()

    is_three = False

    total_count = 0

    for i in range(n):
        if s[i] == '.' and i+1<n and s[i+1] == '.' and i +  2<n and s[i+2] == '.':
            is_three = True
            break
    
        if s[i] == '.':
            total_count += 1

    
    if is_three:
        print("2")
    
    else:
        print(total_count)


def main():
    t = int(sys.stdin.readline())

    if t:
        for _ in range(t):
            solve()

if __name__=="__main__":
    main()

