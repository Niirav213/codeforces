import sys

"""
def solve():
    n,k,q = map(int, sys.stdin.readline().split())

    a = list(map(int, sys.stdin.readline().split()))

    a = [(1 if i <= q else 0) for i in a]
    count1 = 0
    ways = 0

    for i in range(n):
        if a[i] == 1:
            count1 += 1

        else:
            if count1 >= k:
                diff = count1 -k + 1
                ways += (diff * (diff + 1 )) // 2
            count1 = 0

    if count1 >= k:
        diff = count1 - k + 1
        ways += (diff * (diff + 1 )) // 2
    print(ways)
"""

#def main():
#    l = int(sys.stdin.readline())
#
#    if l:
#        for _ in range(l):
#            solve()

#if __name__=="__main__":
    #main()
l = int(sys.stdin.readline())
for _ in range(l):
    n,k,q = map(int, sys.stdin.readline().split())

    a = list(map(int, sys.stdin.readline().split()))

    a = [(1 if i <= q else 0) for i in a]
    count1 = 0
    ways = 0

    for i in range(n):
        if a[i] == 1:
            count1 += 1

        else:
            if count1 >= k:
                diff = count1 -k + 1
                ways += (diff * (diff + 1 )) // 2
            count1 = 0

    if count1 >= k:
        diff = count1 - k + 1
        ways += (diff * (diff + 1 )) // 2
    print(ways)