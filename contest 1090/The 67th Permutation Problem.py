import sys
def solve():
    try:
        n = int(sys.stdin.readline().strip())
        if not n:
            return
    except ValueError:
        return
    
    permutations = []
    
    for i in range(1, n + 1):
        small = i
        median = n + 2*i - 1
        large = n + 2*i

        permutations.extend([small, median, large])
    
    result = []

    result.append(" ".join(map(str, permutations)))
    sys.stdout.write("\n".join(result) + "\n")

def main():
    num = int(sys.stdin.readline().strip())
    if num:
        for _ in range(num):
            solve()

if __name__=="__main__":
    main()