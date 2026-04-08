import sys

def solve():
    try:
        l1 = sys.stdin.readline().split()
        arr = sys.stdin.readline()
        if not arr:
            return
        
    except ValueError:
        return
    
    n,s,x = int(l1[0]), int(l1[1]), int(l1[2])
    arr = list(map(int, arr.split()))

    a = sum(arr)

    if s >= a and (s - a) % x == 0:
        print("yes")
        return
    print("no")
    return

def main():
    num = int(sys.stdin.readline().strip())
    if num:
        for i in range(num):
            solve()


if __name__=="__main__":
    main()