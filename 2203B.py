import sys

def solve():
    n = sys.stdin.readline().strip()
    a = []
    for i in n:
        a.append(int(i))
    
    b = []
    for i in range(len(a)):
        if i == 0:
            b.append(a[i] - 1)
        else:
            b.append(a[i])
    
    a_sum = sum(a)
    b_sum = 0
    k = 0
    b.sort()
    while a_sum > 9:
        a_sum -= b.pop()
        k += 1
    print(k)

if __name__=="__main__":
    l = int(sys.stdin.readline().strip())
    for _ in range(l):
        solve()
