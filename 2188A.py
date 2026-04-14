import sys

def solve():

    try:
        n = int(sys.stdin.readline().strip())
        if not n:
            return
        
    except ValueError:
        return
    
    p = [0] * (n+1)
    used = [False] * (n + 1)

    p[n] = 1
    used[1] = True

    for i in range(n - 1, 0, -1):
        found = False
        for x in range(n, 0, -1):
            if not used[x]:
                if abs(x - p[i+1]) % i == 0:
                    p[i] = x
                    used[x] = True
                    found = True
                    break

    print(*(p[1:]))
    return

def main():
    num = int(sys.stdin.readline().strip())
    if num:
        for _ in range(num):
            solve()

if __name__=="__main__":
    main()    

        