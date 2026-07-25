import sys

data = sys.stdin.read().split()
idx = 0

t = int(data[idx])
idx += 1

for _ in range(t):
    n,k = int(data[idx]), int(data[idx+1])
    idx += 2
    a = []
    for _ in range(n*n):
        a.append(data[idx])
        idx += 1
    

    diff = 0

    left =0
    right = n * n - 1

    while left < right:
        if a[left] != a[right]:
            diff += 1
        left += 1
        right -= 1
                
        if diff > k:
            break
    if diff > k:
        print("NO")
    else:
        remaining = k - diff
        if remaining % 2 == 1 and n % 2 == 0:

            print("NO")
        else:
            print("YES")
            