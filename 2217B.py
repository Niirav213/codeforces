import sys

def solve():

    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))

    p = int(sys.stdin.readline().strip())
    arr = [0] * (n+2)
    for i in range(1, n+1):
        arr[i] = a[i-1]
    arr[0] = arr[p]
    arr[n+1] = arr[p]

    countL = 0
    for i in range(0,p):
        if arr[i] != arr[i+1]:
            countL +=1
    
    countR =0
    for i in range(p, n+1):
        if arr[i] != arr[i+1]:
            countR += 1

    print(max(countL,countR))

def main():
    line = int(sys.stdin.readline())
    if line:
        for _ in range(line):
            solve()

if __name__=="__main__":
    main() 
