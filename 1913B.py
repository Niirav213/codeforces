import sys

def solve():
    s = sys.stdin.readline().strip()
    n = len(s)
    count0, count1 = 0,0

    for char in s:
        if char == '1':
            count1 += 1
        else:
            count0 += 1
    
    len_t = 0

    for i in s:
        if i == '1' and count0 > 0:
            len_t += 1
            count0 -= 1
        elif i == '0' and count1 > 0:
            len_t += 1
            count1 -= 1
        else:
            break
    
    print(n - len_t)

def main():
    l = int(sys.stdin.readline())
    if l:
        for _ in range(l):
            solve()


if __name__=="__main__":
    main()