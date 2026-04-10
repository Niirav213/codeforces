import sys

def solve():
    try:
        len = int(sys.stdin.readline().strip())
        str = sys.stdin.readline().strip()
        if not len:
            return
    
    except ValueError:
        return
    
    score = 0
    for _ in range(len):
        blocks = len
        for i in range(1,len):
            
            if str[i] == str[i - 1]:
                blocks -= 1

        if blocks > score:
            score = blocks

        str = str[1:] + str[0]
    print(score)
    return

def main():
    try:
        test_cases = int(sys.stdin.readline().strip())
        if test_cases:
            for _ in range(test_cases):
                solve()
    except ValueError:
        return
    
if __name__=="__main__":
    main()