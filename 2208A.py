import sys

def solve():
    input_data = sys.stdin.read().split()

    if not input_data:
        return
    
    it = iter(input_data)

    try:
        # Read number of test cases
        testcases = int(next(it))
    except StopIteration:
        return

    for _ in range(testcases):
        try:
            n = int(next(it))
            # The original code uses a fixed array of 10005. 
            # In Python, a dictionary is more flexible for frequency counting.
            cnt = {}
            flag = True
            limit = n * (n - 1)
            
            for _ in range(n * n):
                val = next(it)
                cnt[val] = cnt.get(val, 0) + 1
                
                if cnt[val] > limit:
                    flag = False
                    # We continue consuming the input for this test case 
                    # to keep the iterator in the correct position
            
            if flag:
                sys.stdout.write("YES\n")
            else:
                sys.stdout.write("NO\n")
                
        except StopIteration:
            break

if __name__ == "__main__":
    solve()