import sys



def solve():
    s = sys.stdin.readline().strip()

    n = len(s)
    s2 = s + s
    max_len = 0
    curr_len = 0

    for i in s2:
        if i =='1':
            curr_len += 1
            max_len= max(max_len, curr_len)
        else:
            curr_len =0
    if max_len >n:
        max_len = n
    
    if max_len == n:
        print(n*n)
        
    
    else:
        width = (max_len + 1) // 2
        hight =(max_len + 2) // 2
        print(width * hight)

    
    

if __name__=="__main__":
    l = int(sys.stdin.readline())

    for _ in range(l):
        solve()
