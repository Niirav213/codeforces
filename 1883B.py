import sys

def solve():
    n,k = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()

    char_freq = [0] * 26
    for char in s:
        char_freq[ord(char) - ord('a')] += 1
    odd_freq = 0

    for freq in char_freq:
        odd_freq += freq % 2
    if odd_freq > k + 1:
        print("NO")
    else:
        print("YES")

def main():
    l = int(sys.stdin.readline())

    if l:
        for _ in range(l):
            solve()

if __name__=="__main__":
    main()