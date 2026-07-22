import sys


data = sys.stdin.read().split()
idx = 0

t = int(data[idx])
idx += 1

for _ in range(t):
    n = int(data[idx])
    idx += 1

    mat = []

    for _ in range(n):
        mat.append(data[idx])
        idx += 1
    
    ans = 0

    for i in range(n):
        for j in range(n):

            c0,c1 = 0,0

            if mat[i][j] == '0':
                c0 += 1
            else:
                c1 += 1
            
            if mat[j][n - i - 1] == '0':
                c0 += 1
            else:
                c1 += 1
            
            if mat[n-i-1][n-j-1] == '0':
                c0 += 1
            else:
                c1 += 1
            
            if mat[n - j - 1][i] == '0':
                c0 += 1
            else:
                c1 += 1
            
            if c0 == 0 or c1 == 0:
                continue

            if c0 >= c1:
                ans += c1
                mat[i] = mat[i][:j] + '0'+ mat[i][j+1:]
                mat[j] = mat[j][:n - i -1] + '0' + mat[j][n-i:]
                mat[n-i-1] = mat[n-i-1][:n-j-1] + '0' + mat[n-i-1][n-j:]
                mat[n-j-1] = mat[n-j-1][:i] + '0' + mat[n-j-1][i+1:]
            else:
                ans += c0
                mat[i] = mat[i][:j] + '1'+ mat[i][j+1:]
                mat[j] = mat[j][:n - i -1] + '1' + mat[j][n-i:]
                mat[n-i-1] = mat[n-i-1][:n-j-1] + '1' + mat[n-i-1][n-j:]
                mat[n-j-1] = mat[n-j-1][:i] + '1' + mat[n-j-1][i+1:]
    print(ans)