import sys


data = list(map(int, sys.stdin.buffer.read().split()))
idx = 0

t = data[idx]  
idx += 1

out = []

for _ in range(t):
    n = data[idx]  
    idx += 1

    a = data[idx:idx + n]
    idx += n

    a.sort()

    ans = 0
    prev_val = None      
    run_len = 0           
    prev_run_len = 0      

    for x in a:
        if prev_val is None or x != prev_val:
            prev_run_len = run_len if (prev_val is not None and x == prev_val + 1) else 0
            run_len = 0
        run_len += 1
        if run_len > prev_run_len:
            ans += 1
        prev_val = x

    out.append(str(ans))

sys.stdout.write("\n".join(out))
