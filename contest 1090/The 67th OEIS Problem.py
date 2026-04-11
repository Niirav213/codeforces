import sys
def get_primes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    for p in range(2, limit + 1):
        if is_prime[p]:
            primes.append(p)
            if len(primes) > 10001:
                break
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
    return primes

prime_list = get_primes(110000)

def solve():
    try:
        n = int(sys.stdin.readline().strip())
        if not n:
            return
    except ValueError:
        return
    ans = []
    for i in range(n):
        ans.append(prime_list[i] * prime_list[i + 1])
    sys.stdout.write(" ".join(map(str, ans)) + "\n")
    return

def main():
        
        n = int(sys.stdin.readline().strip())
        if n:
             for _ in range(n):
                  solve()

if __name__=="__main__":
     main()