import sys

def solve():
    n = int(sys.stdin.readline())
    s = list(sys.stdin.readline())

    for  i  in range(1,n-1):
        if s[i-1]=='1' and s[i+1]=='1':
            s[i] = '1'
    
    count1 = 0

    for i in range(n):
        if s[i] == '1':
            count1 += 1

    
    for i in range(1,n-1):
        if s[i-1] == '1' and s[i+1] == '1':
            s[i] =0
    
    count0 = 0
    for i in range(n):
        if s[i] == '1':
            count0 += 1
    
    print(count0, count1)

def main():
    line = int(sys.stdin.readline())
    if line:
        for _ in range(line):
            solve()

if __name__=="__main__":
    main()