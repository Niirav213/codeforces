import sys

def solve():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))

    indexed_a = list(enumerate(a))

    indexed_a.sort(key=lambda x:x[1], reverse=True)
    coordinates = [0] * (n+1)
    for rank, (index, freq) in enumerate(indexed_a):

        distance = (rank // 2) + 1

        coordinate = distance if rank % 2 == 0 else -distance

        coordinates[index + 1] = coordinate

    length_traversed = 0
    for i in range(n):
        length_traversed += 2 * abs(coordinates[i+1]) * a[i]
    print(length_traversed)
    print(*(coordinates))

if __name__=="__main__":
    l = int(sys.stdin.readline())

    for _ in range(l):
        solve()