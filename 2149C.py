import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    num_test_cases = int(next(iterator))
    
    out = []
    for _ in range(num_test_cases):
        n = int(next(iterator))
        k = int(next(iterator))
        
        # Frequency array for numbers 0 to k
        freq = [0] * (k + 1)
        
        for _ in range(n):
            x = int(next(iterator))
            if x <= k:
                freq[x] += 1
        
        # Missing numbers are the ones from 0 to k-1 that have a count of 0
        missing_count = freq[:k].count(0)
        countK = freq[k]
        
        out.append(str(max(missing_count, countK)))
        
    print('\n'.join(out))

if __name__ == "__main__":
    main_solve = solve
    main_solve()